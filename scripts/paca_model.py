from functions import delete_files_in_folder, check_model_subfolders, silence_tensorflow, get_test_name
silence_tensorflow()
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard, EarlyStopping
from tensorflow.keras.mixed_precision import experimental as mixed_precision
from environ import (test_var, directory_dict, random_seed,  back_test_days, save_logs,
defaults)
from time_functs import get_time_string
from paca_model_functs import (load_data, create_model, predict, accuracy_score, plot_graph, 
get_accuracy, nn_report, return_real_predict, get_all_accuracies, get_all_maes)
from datetime import datetime
import numpy as np
import pandas as pd
import random
import sys
import time
import os


def decision_neural_net(symbol, end_date=None, params=defaults):
    start_time = time.time()
    data, model, test_acc, valid_acc, train_acc, test_mae, valid_mae, train_mae, epochs_used = make_neural_net(
        symbol, end_date, params
    )

    end_time = time.time()
    total_time = end_time - start_time
    percent = nn_report(symbol, total_time, model, data, test_acc, valid_acc, train_acc, params["N_STEPS"])

    return percent, test_acc


def tuning_neural_net(symbol, end_date=None, params=defaults):
    
    data, model, test_acc, valid_acc, train_acc, test_mae, valid_mae, train_mae, epochs_used = make_neural_net(
        symbol, end_date, params
    )
    
    return test_acc, valid_acc, train_acc, test_mae, valid_mae, train_mae, epochs_used

def saveload_neural_net(symbol, end_date=None, params=defaults):

    data, model, test_acc, valid_acc, train_acc, test_mae, valid_mae, train_mae, epochs_used = make_neural_net(
        symbol, end_date, params    
    )

    return epochs_used

def make_neural_net(symbol, end_date, params):
    #description of all the parameters used is located inside environment.py
    os.environ["TF_XLA_FLAGS"] = "--tf_xla_auto_jit=2 --tf_xla_cpu_global_jit" # turns on xla and cpu xla
 
    gpus = tf.config.experimental.list_physical_devices("GPU")

    if gpus:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)

    tf.keras.backend.clear_session()
    tf.keras.backend.reset_uids()
   
    tf.config.optimizer.set_jit(True)

    
    # policy = mixed_precision.Policy("mixed_float16")
    # mixed_precision.set_policy(policy)

    # set seed, so we can get the same results after rerunning several times
    np.random.seed(random_seed)
    tf.random.set_seed(random_seed)
    random.seed(random_seed)
    
    check_model_subfolders(params["SAVE_FOLDER"])
    
    # model name to save, making it as unique as possible based on parameters
    model_name = (symbol + "-" + get_test_name(params))

    data, train, valid, test = load_data(symbol, end_date, params["N_STEPS"], params["BATCH_SIZE"], 
    params["LIMIT"], params["FEATURE_COLUMNS"])

    model = create_model(params["N_STEPS"], params["UNITS"], params["CELL"], params["N_LAYERS"], 
    params["DROPOUT"], params["LOSS"], params["OPTIMIZER"], params["BIDIRECTIONAL"])

    logs_dir = "logs/" + get_time_string() + "-" + params["SAVE_FOLDER"]

    if params["SAVELOAD"]:
        checkpointer = ModelCheckpoint(directory_dict["model_directory"] + "/" + params["SAVE_FOLDER"] + "/" + model_name + ".h5", save_weights_only=True, save_best_only=True, verbose=1)
    else:    
        checkpointer = ModelCheckpoint(os.path.join("results", model_name + ".h5"), save_weights_only=True, save_best_only=True, verbose=1)
    
    if save_logs:
        tboard_callback = TensorBoard(log_dir=logs_dir, profile_batch="1000, 1200") 
    else:
        tboard_callback = TensorBoard(log_dir=logs_dir, profile_batch=0)

        early_stop = EarlyStopping(patience=params["PATIENCE"])
    
    history = model.fit(train,
        batch_size=params["BATCH_SIZE"],
        epochs=params["EPOCHS"],
        verbose=2,
        use_multiprocessing=True,
        workers=10,
        validation_data=valid,
        callbacks = [tboard_callback, checkpointer, early_stop]   
    )

    epochs_used = len(history.history["loss"])

    #before testing, no shuffle
    if params["SAVELOAD"]:
        test_acc = valid_acc = train_acc = test_mae = valid_mae = train_mae = 0    
    else:    
        data, train, valid, test = load_data(symbol, end_date, params["N_STEPS"], params["BATCH_SIZE"], 
            params["LIMIT"], params["FEATURE_COLUMNS"], False
        )

        model_path = os.path.join("results", model_name + ".h5")
        model.load_weights(model_path)

        test_mae, valid_mae, train_mae = get_all_maes(model, test, valid, train, data) 

        delete_files_in_folder(directory_dict["results_directory"])
        os.rmdir(directory_dict["results_directory"])
        
        train_acc, valid_acc, test_acc = get_all_accuracies(model, data, params["LOOKUP_STEP"])

    if not save_logs:
        delete_files_in_folder(logs_dir)
        os.rmdir(logs_dir)

    return data, model, test_acc, valid_acc, train_acc, test_mae, valid_mae, train_mae, epochs_used
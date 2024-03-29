from config.silen_ten import silence_tensorflow
silence_tensorflow()
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard, EarlyStopping
from tensorflow.keras import mixed_precision
from config.environ import directory_dict, random_seed, save_logs, defaults, random_seed
from functions.functions import delete_files_in_folder, check_model_folders, get_model_name
from functions.time import get_time_string, get_past_date_string
from functions.functions import get_model_name, sr2, r0
from functions.paca_model import create_model, get_accuracy, get_current_price, predict, return_real_predict
from functions.io import save_prediction, load_saved_predictions
from functions.all_2D_models import DTREE, MLENS, RFORE, KNN, ADA, XGB, XTREE, BAGREG, MLP
from scipy.signal import savgol_filter
from statistics import mean
import talib as ta
import numpy as np
import multiprocessing
import copy
import sys
import gc
import random
import os


def nn_train_save(symbol, params=defaults, predictor="nn1", data_dict={}):
    #description of all the parameters used is located inside environment.py
    

    gc.collect()
    tf.keras.backend.clear_session()
    tf.keras.backend.reset_uids()

    # policy = mixed_precision.Policy("mixed_float16")
    # mixed_precision.set_global_policy(policy)
    options = {"shape_optimization": True}
    tf.config.optimizer.set_experimental_options(options)
    os.environ["TF_XLA_FLAGS"] = "--tf_xla_auto_jit=2, --tf_xla_cpu_global_jit" # turns on xla and cpu xla
    tf.config.optimizer.set_jit(True)

    # set seed, so we can get the same results after rerunning several times
    np.random.seed(random_seed)
    tf.random.set_seed(random_seed)
    random.seed(random_seed)

    nn_params = params[predictor]
    
    check_model_folders(params["SAVE_FOLDER"], symbol)
   
    model_name = (symbol + "-" + get_model_name(nn_params))

    model = create_model(nn_params)

    logs_dir = "logs/" + get_time_string() + "-" + params["SAVE_FOLDER"]

    if save_logs:
        tboard_callback = TensorBoard(log_dir=logs_dir, profile_batch="200, 1200") 
    else:
        tboard_callback = TensorBoard(log_dir=logs_dir, profile_batch=0)


    if nn_params['TEST_SIZE'] != 1: # Using validation
        checkpointer = ModelCheckpoint(f"{directory_dict['model']}/{params['SAVE_FOLDER']}/{model_name}.h5", 
            save_weights_only=True, save_best_only=True, verbose=1)

        early_stop = EarlyStopping(patience=nn_params['PATIENCE'])
        
        history = model.fit(data_dict['train'],
            batch_size=nn_params['BATCH_SIZE'],
            epochs=nn_params['EPOCHS'],
            verbose=2,
            validation_data=data_dict['valid'],
            callbacks = [tboard_callback, checkpointer, early_stop]   
        )
    
    else: # Not using validation
        checkpointer = ModelCheckpoint(f"{directory_dict['model']}/{params['SAVE_FOLDER']}/{model_name}.h5", 
            save_freq=50, save_weights_only=True, verbose=1)

        history = model.fit(data_dict['train'],
            batch_size=nn_params['BATCH_SIZE'],
            epochs=nn_params['EPOCHS'],
            verbose=2,
            callbacks = [tboard_callback, checkpointer]   
        )

    epochs_used = copy.copy(len(history.history['loss']))


    if not save_logs:
        delete_files_in_folder(logs_dir)
        os.rmdir(logs_dir)

    return epochs_used

def configure_gpu():
    gpus = tf.config.experimental.list_physical_devices("GPU")

    if gpus:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)

def nn_load_predict(symbol, params, predictor, data_dict, to_print=False):
    model = create_model(params[predictor])
    model.load_weights(directory_dict["model"] + "/" + params["SAVE_FOLDER"] + "/" + 
        symbol + "-" + get_model_name(params[predictor]) + ".h5")
    predicted_value = predict(model, data_dict["result"], params[predictor]["N_STEPS"], params[predictor]["TEST_VAR"],
        layer=params[predictor]["LAYERS"][0])
    # print(f"inside nn_load_predict {predicted_value} {type(predicted_value)}")

    return predicted_value

def ensemble_predictor(symbol, params, current_date, data_dict, df):
    ensemb_predict_list = []
    epochs_dict = {}
    
    if not params["TRADING"]:
        if current_date:
            s_current_date = get_past_date_string(current_date)
        for predictor in params['ENSEMBLE']:
            if "nn" in predictor:
                epochs_dict[predictor] = 0
                if not symbol in params[predictor]['SAVE_PRED']:
                    params[predictor]['SAVE_PRED'][symbol] = {}
                if not s_current_date in params[predictor]['SAVE_PRED'][symbol]:
                    params[predictor]['SAVE_PRED'][symbol][s_current_date] = {}

    current_price = get_current_price(df)

    classifying = False
    for predictor in params['ENSEMBLE']:
        if params[predictor]['TEST_VAR'] == "acc":
            classifying = True
            break

    for predictor in params['ENSEMBLE']:
        if predictor == "7MA":
            df['7MA'] = df.c.rolling(window=7).mean()
            predicted_value = np.float32(df["7MA"][len(df.c) - 1])
            
        elif predictor == "lin_reg":
            df['lin_reg'] = ta.LINEARREG(df.c, timeperiod=7)
            predicted_value = np.float32(df.lin_reg[len(df.c) - 1])

        elif predictor == "sav_gol":
            df["s.c"] = savgol_filter("s", "c")
            predicted_value = np.float32(df.sc[len(df.c) - 1])

        elif predictor == "EMA":
            df['EMA'] = ta.EMA(df.c, timeperiod=5)
            predicted_value = np.float32(df["EMA"][len(df.c) - 1])

        elif "DTREE" in predictor:
            predicted_value = DTREE(params, predictor, data_dict)
        elif "XTREE" in predictor:
            predicted_value = XTREE(params, predictor, data_dict)
        elif "RFORE" in predictor:
            predicted_value = RFORE(params, predictor, data_dict)
        elif "KNN" in predictor:
            predicted_value = KNN(params, predictor, data_dict)
        elif "ADA" in predictor:
            predicted_value = ADA(params, predictor, data_dict)
        elif "XGB" in predictor:
            predicted_value = XGB(params, predictor, data_dict)
        elif "BAGREG" in predictor:
            predicted_value = BAGREG(params, predictor, data_dict)
        elif "MLP" in predictor:
            predicted_value = MLP(params, predictor, data_dict)
        elif "MLENS" in predictor:
            predicted_value = MLENS(params, predictor, data_dict)
                    
        elif "nn" in predictor:
            if params['TRADING']:
                predicted_value = nn_load_predict(symbol, params, predictor, data_dict[predictor])
            else:
                if load_saved_predictions(symbol, params, current_date, predictor):
                    predicted_value, epochs_run = load_saved_predictions(symbol, params, current_date, predictor)
                    epochs_dict[predictor] = epochs_run
                else:
                    epochs_run = nn_train_save(symbol, params, predictor, data_dict[predictor])
                    epochs_dict[predictor] = epochs_run
                    predicted_value = nn_load_predict(symbol, params, predictor, data_dict[predictor])
                    save_prediction(symbol, params, current_date, predictor, predicted_value, epochs_run)
        else:
            print("\nPREDICTOR NOT RECOGNIZED")
            print("GET YO SHIT TOGETHER\n")
            sys.exit(-1)
        

        if params[predictor]['TEST_VAR'] == "pc.c":
            predicted_value = current_price * 1 + predicted_value
        elif params[predictor]['TEST_VAR'] == "d.c":
            predicted_value = current_price + predicted_value

        if classifying:
            # print(type(predicted_value))
            # print(predicted_value != 1)
            if predicted_value != 0 and predicted_value != 1:
                # print("shouldn't be here")
                # print(predicted_value > current_price, predicted_value)
                if predicted_value > current_price:
                    ensemb_predict_list.append(1)
                else:
                    ensemb_predict_list.append(0)
            else:
                ensemb_predict_list.append(predicted_value)

        else:
            ensemb_predict_list.append(np.float32(predicted_value))

    print(f"Ensemble prediction list: {ensemb_predict_list}")
    if classifying:
        if len(ensemb_predict_list) % 2 == 0:
            print("\nDEAR GOD, you making a majority voting ensemble with an even amount of ensembles.")
            print("Shame on you, try agin!")
            sys.exit(-1)
        final_prediction = r0(mean(ensemb_predict_list))

    else:
        final_prediction = mean(ensemb_predict_list)

    print(f"The final prediction: {sr2(final_prediction)}")

    return final_prediction, current_price, epochs_dict


def ensemble_accuracy(symbol, params, current_date, classification=False):
    data = {}
    for predictor in params:
        if "nn" in predictor:
            pass
            # data, model = load_model_with_data(symbol, current_date, params, predictor)
            model = {}
            # get_all_accuracies(model, data, params[predictor["LOOKUP_STEP"]], params[predictor["TEST_VAR"]])

            y_train_real, y_train_pred = return_real_predict(model, data["X_train"], data["y_train"], 
            data["column_scaler"][params[predictor["TEST_VAR"]]], classification)
            print(f"{y_train_real, y_train_pred}")
            y_valid_real, y_valid_pred = return_real_predict(model, data["X_valid"], data["y_valid"], 
            data["column_scaler"][params[predictor["TEST_VAR"]]], classification)
            y_test_real, y_test_pred = return_real_predict(model, data["X_test"], data["y_test"],
            data["column_scaler"][params[predictor["TEST_VAR"]]], classification)





    train_acc = get_accuracy(y_train_real, y_train_pred, params[predictor["LOOKUP_STEP"]])
    valid_acc = get_accuracy(y_valid_real, y_valid_pred, params[predictor["LOOKUP_STEP"]])
    test_acc = get_accuracy(y_test_real, y_test_pred, params[predictor["LOOKUP_STEP"]])
    




    return train_acc, valid_acc, test_acc 

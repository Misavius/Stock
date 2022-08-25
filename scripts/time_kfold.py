from config.silen_ten import silence_tensorflow
silence_tensorflow()
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard, EarlyStopping
from tensorflow.keras.layers import Dense
from tensorflow.python.data import Dataset
from tensorflow.python.data.experimental import AUTOTUNE
from sklearn.model_selection import TimeSeriesSplit
from config.environ import save_logs, directory_dict
from config.symbols import sym_dict
from config.model_repository import models
from functions.data_load import get_proper_df, load_all_data, preprocess_dfresult, construct_3D_np
from functions.functions import check_directories, check_model_folders, get_model_name, delete_files_in_folder, r1002
from functions.time import get_current_datetime
from functions.tuner import get_user_input
from functions.paca_model import create_model, get_accuracy, return_real_predict
from functions.time import get_time_string, get_current_datetime
from paca_model import configure_gpu
import numpy as np
import os


def time_kfold(params):
    configure_gpu()

    kfold_symbols, params = get_user_input(sym_dict, params)
    

    for symbol in kfold_symbols:
        predictor = params["ENSEMBLE"][0]
        scale = True
        to_print = True


        df = get_proper_df(symbol, params[predictor]["LIMIT"], "V2")
        data_dict = load_all_data(symbol, params, df, get_current_datetime())


        tt_df, result = preprocess_dfresult(params[predictor], df, get_current_datetime(), scale=scale, to_print=to_print)
        if params[predictor]['LAYERS'][0][1] == Dense:
            tt_df = tt_df.dropna()
            y = tt_df["future"]
            tt_df = tt_df.drop(columns="future")
            X = tt_df.to_numpy()

            X = np.array(X)
            y = np.array(y)
        else:
            X, y = construct_3D_np(tt_df, params[predictor], result)
        print(len(X), len(y))

        num_splits = 10

        accuracies = []
        # kfold = KFold(n_splits=num_splits, shuffle=True)
        kfold = TimeSeriesSplit(n_splits=num_splits)
        i = 0
        for train, test in kfold.split(X, y):
            print(f" IIIIIIIIIIIIIIII {i} \n\n ")
            print(f"len of train {len(X[train])}")
            print(f"len of test {len(y[test])}")
            print(f"what we're selecting {test}")
            i += 1

            train = Dataset.from_tensor_slices((X[train], y[train]))
            valid = Dataset.from_tensor_slices((X[test], y[test]))

            train = train.batch(params[predictor]["BATCH_SIZE"])
            valid = valid.batch(params[predictor]["BATCH_SIZE"])

            train = train.cache()
            valid = valid.cache()

            train = train.prefetch(buffer_size=AUTOTUNE)
            valid = valid.prefetch(buffer_size=AUTOTUNE)

            data_dict["train"] = train
            data_dict["valid"] = valid

            # epochs = nn_train_save(symbol, params, predictor=predictor)
            nn_params = params[predictor]
            
            check_model_folders(params["SAVE_FOLDER"], symbol)

            model_name = (symbol + "-" + get_model_name(nn_params))


            model = create_model(nn_params)

            logs_dir = "logs/" + get_time_string() + "-" + params["SAVE_FOLDER"]

            checkpointer = ModelCheckpoint(directory_dict["model"] + "/" + params["SAVE_FOLDER"] + "/" 
                + model_name + ".h5", save_weights_only=True, save_best_only=True, verbose=1)
            
            if save_logs:
                tboard_callback = TensorBoard(log_dir=logs_dir, profile_batch="200, 1200") 
            else:
                tboard_callback = TensorBoard(log_dir=logs_dir, profile_batch=0)

            # early_stop = EarlyStopping(patience=nn_params["PATIENCE"])
            
            history = model.fit(data_dict["train"],
                batch_size=nn_params["BATCH_SIZE"],
                epochs=nn_params["EPOCHS"],
                verbose=0,
                validation_data=data_dict["valid"],
                callbacks = [tboard_callback, checkpointer]   
            )

            epochs_used = len(history.history["loss"])
                
            if not save_logs:
                delete_files_in_folder(logs_dir)
                os.rmdir(logs_dir)


            print(result["column_scaler"])
            y_real, y_pred = return_real_predict(model, X[test], y[test], result['column_scaler']['future'])

            # y_real = y[test]
            # y_pred = model.predict(X[test])
            acc = get_accuracy(y_pred, y_real, lookup_step=1)
            print(r1002(acc))
            accuracies.append(acc)
            model.evaluate(valid)


        overall_acc = r1002(sum(accuracies) / num_splits)
        print(overall_acc)

if __name__ == "__main__":
    check_directories()
    params = {
        "ENSEMBLE": ["nn8"],
        "TRADING": False,
        "SAVE_FOLDER": "",
        "LIMIT": 4000,
    }

    for model in params["ENSEMBLE"]:
        if model in models:
            params[model] = models[model]

    print(params)

    time_kfold(params)

    
            

from config.environ import directory_dict
from config.api_key import alpha_key
from functions.time_functs import make_Timestamp, get_trade_day_back, get_full_end_date
from functions.error_functs import  net_error_handler, keyboard_interrupt
from functions.trade_functs import get_api
from functions.time_functs import modify_timestamp, get_current_datetime, get_past_datetime
from functions.functions import layer_name_converter
from functions.tech_functs import techs_dict
from functions.io_functs import save_to_dictionary, read_saved_contents
from tensorflow.data import Dataset
from tensorflow.data.experimental import AUTOTUNE
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from scipy.signal import savgol_filter, cwt
from collections import deque
from alpaca_trade_api.rest import TimeFrame
import talib as ta
import pandas as pd
import numpy as np
import datetime
import time
import copy
import requests
import os



def alpaca_date_converter(df):
    df.index = df["time"]
    df = df.drop("time", axis=1)
    return df


def modify_dataframe(features, df):
    base_features = ["o", "c", "l", "h", "v"]
    removable_features = ["o", "l", "h", "v", "tc", "vwap", "adj_c", "div", "split"]
    for feature in features:
        # print(f"we got feature {feature}")
        if feature not in base_features:
            if feature in techs_dict:
                # print(f"we got feature {feature} here, yeah yeah")
                techs_dict[feature]["function"](feature, df)
            else:
                print("Feature is not in the technical indicators dictionary. That sucks, probably")
    for feature in removable_features:
        if feature not in features and feature in list(df.columns):
            df = df.drop(columns=[feature])

    # pd.set_option("display.max_columns", None)
    # pd.set_option("display.max_rows", None)
    # print(df.head(1))
    # print(df.tail(1))
    # print(df)

    return df

def scale_data(df, result):
    column_scaler = {}
    for column in df.columns:
        scaler = preprocessing.MinMaxScaler()
        df[column] = scaler.fit_transform(np.expand_dims(df[column].values, axis=1))
        column_scaler[column] = scaler

    result["column_scaler"] = column_scaler
    return result

def get_alpaca_df(symbol, limit=1000, to_print=True):
    api = get_api()
    no_connection = True
    end = get_current_datetime()
    start = get_past_datetime(2000, 1, 1)
    while no_connection:
        try:
            # print(f"limit{limit} end{end} start{start}")
            s = time.perf_counter()
            # df = get_alpaca_data(symbol, end_date, api, limit=limit)
            df = api.get_bars(symbol, start=start, end=end, timeframe=TimeFrame.Day, 
                limit=limit).df
            df = df.rename(columns={"open": "o", "high":"h", "low": "l", "close": "c",
                "volume": "v", "trade_count": "tc"})
            no_connection = False
            # print(f"all loading took {time.perf_counter() - s}")
        except KeyboardInterrupt:
            keyboard_interrupt()
        except Exception:
            net_error_handler(symbol, Exception)

    return df

def get_alpha_df(symbol, output_size):
    load_dictionary = {
        "o": {},
        "h": {},
        "l": {},
        "c": {},
        "adj_c": {},
        "v": {},
        "div": {},
        "split": {}
    }
    if os.path.isfile(f"""{directory_dict["data"]}/{symbol}.txt"""):
        load_dictionary = read_saved_contents(f"""{directory_dict["data"]}/{symbol}.txt""", load_dictionary)
        df = pd.DataFrame(load_dictionary, dtype=np.float32)
        # TODO check for whether or not this is up to date and then update it
    else:
        no_connection = False
        while no_connection:
            try:
                df = download_alpha_df(symbol, output_size)
                no_connection = True
            except KeyboardInterrupt:
                keyboard_interrupt()
            except Exception:
                net_error_handler(symbol, Exception)

    return df

def download_alpha_df(symbol, output_size):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize={output_size}&apikey={alpha_key}"
    no_connection = True
    while no_connection:
        try:
            r = requests.get(url)
            no_connection = False
        except KeyboardInterrupt:
            keyboard_interrupt()
        except Exception:
            net_error_handler(symbol, Exception)

    data = r.json()
    df = pd.DataFrame(data["Time Series (Daily)"], dtype=np.float32)
    df = df.transpose()
    df = df.rename(columns={"1. open": "o", "2. high": "h", "3. low": "l", "4. close": "c", "5. adjusted close": "adj_c",
        "6. volume": "v", "7. dividend amount": "div","8. split coefficient": "split"})
    print(df.head(1))
    print(df.tail(1))
    df_dict = df.to_dict()
    save_to_dictionary(f"""{directory_dict["data"]}/{symbol}.txt""", df_dict)
    
    return df

def get_proper_df(symbol, limit, option):
    if option == "training":
        df = get_alpha_df(symbol, "full")
    elif option == "running":
        df = get_alpaca_df(symbol, limit, to_print=True)

    return df

def load_all_data(params, df):
    data_dict = {}
    req_2d = ["DTREE1", "RFORE1", "KNN1"]
    types_to_load = []

    for predictor in params["ENSEMBLE"]:
        if predictor in req_2d and "2D" not in types_to_load:
            result = load_2D_data(params[predictor], df, tensorify=False)
            data_dict[predictor] = result
        elif "nn" in predictor:
            if (layer_name_converter(params[predictor]["LAYERS"][0]) == "Dense"
                and "2D_tensor" not in types_to_load):
                result, train, valid, test = load_2D_data(params[predictor], df, tensorify=True)
                data_dict[predictor] = {"result": result, "train": train, "valid": valid,
                    "test": test}
            elif "3D_tensor" not in types_to_load:
                result, train, valid, test = load_3D_data(params[predictor], df)
                data_dict[predictor] = {"result": result, "train": train, "valid": valid,
                    "test": test}

    return data_dict

def preprocess_dfresult(params, df, scale, to_print):
    tt_df = copy.deepcopy(df)
    if to_print:
        print(f"""Included features: {params["FEATURE_COLUMNS"]}""")

    tt_df = modify_dataframe(params["FEATURE_COLUMNS"], tt_df)
    for col in params["FEATURE_COLUMNS"]:
        assert col in tt_df.columns, f"'{col}' does not exist in the dataframe."

    tt_df["future"] = tt_df[params["TEST_VAR"]].shift(-params["LOOKUP_STEP"])
    if "c" not in params["FEATURE_COLUMNS"]:
        tt_df = tt_df.drop(columns=["c"])

    result = {}
    if scale:
        result = scale_data(tt_df, result)

    return tt_df, result

def load_3D_data(params, df=None, shuffle=True, scale=True, to_print=True):
    tt_df, result = preprocess_dfresult(params, df, scale=scale, to_print=to_print)
    
    # last `lookup_step` columns contains NaN in future column
    # get them before droping NaNs
    last_sequence = np.array(tt_df[params["FEATURE_COLUMNS"]].tail(params["LOOKUP_STEP"]))
    # drop NaNs
    tt_df.dropna(inplace=True)
    sequence_data = []
    sequences = deque(maxlen=params["N_STEPS"])
    for entry, target in zip(tt_df[params["FEATURE_COLUMNS"]].values, tt_df["future"].values):
        sequences.append(entry)
        if len(sequences) == params["N_STEPS"]:
            sequence_data.append([np.array(sequences), target])
    # get the last sequence by appending the last `n_step` sequence with `lookup_step` sequence
    # for instance, if n_steps=50 and lookup_step=10, last_sequence should be of 59 (that is 50+10-1) length
    # this last_sequence will be used to predict in future dates that are not available in the dataset
    last_sequence = list(sequences) + list(last_sequence)
    # shift the last sequence by -1
    last_sequence = np.array(pd.DataFrame(last_sequence).shift(-1).dropna())
    # add to result
    result["last_sequence"] = last_sequence
    # print(last_sequence)
    # construct the X"s and y"s
    X, y = [], []
    
    for seq, target in sequence_data:
        X.append(seq)
        y.append(target)

    X = np.array(X)
    y = np.array(y)
    # reshape X to fit the neural network
    X = X.reshape((X.shape[0], X.shape[2], X.shape[1]))

    result = split_data(X, y, params["TEST_SIZE"], shuffle, result)    

    train, valid, test = make_tensor_slices(params, result)

    return result, train, valid, test


def load_2D_data(params, df=None, shuffle=True, scale=True, tensorify=False, to_print=True):
    tt_df, result = preprocess_dfresult(params, df, scale, to_print)

    tt_df.dropna(inplace=True)
    y = tt_df["future"]
    tt_df = tt_df.drop(columns="future")
    X = tt_df.to_numpy()

    X = np.array(X)
    y = np.array(y)
    
    result = split_data(X, y, params["TEST_SIZE"], shuffle, result)    

    if tensorify:
        train, valid, test = make_tensor_slices(params, result)
        return result, train, valid, test
    else:
        return result

def split_data(X, y, test_size, shuffle, result):
    # print(f"""before split {len(X)}""")
    result["X_train"], result["X_test"], result["y_train"], result["y_test"] = train_test_split(X, y, test_size=2, random_state=42, 
        shuffle=False)
    # print(f"""len train{len(result["X_train"])}  len test {len(result["X_test"])}""")
    result["X_train"], result["X_valid"], result["y_train"], result["y_valid"] = train_test_split(result["X_train"], result["y_train"],
        test_size=test_size, random_state=42, shuffle=shuffle)
    # print(f"""len train{len(result["X_train"])} len valid {len(result["X_valid"])} len test {len(result["X_test"])}""")
    # print(result["X_test"])
    # print(f"""result["y_test"] {result["y_test"]}""")

    return result

def make_tensor_slices(params, result):
    train = Dataset.from_tensor_slices((result["X_train"], result["y_train"]))
    valid = Dataset.from_tensor_slices((result["X_valid"], result["y_valid"]))
    test = Dataset.from_tensor_slices((result["X_test"], result["y_test"]))

    train = train.batch(params["BATCH_SIZE"])
    valid = valid.batch(params["BATCH_SIZE"])
    test = test.batch(params["BATCH_SIZE"])
    
    train = train.cache()
    valid = valid.cache()
    test = test.cache()

    train = train.prefetch(buffer_size=AUTOTUNE)
    valid = valid.prefetch(buffer_size=AUTOTUNE)
    test = test.prefetch(buffer_size=AUTOTUNE)

    return train, valid, test



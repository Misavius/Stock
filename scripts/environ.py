import os
import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)
logging.getLogger("tensorflow").addHandler(logging.NullHandler(logging.ERROR))
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from tensorflow.keras.layers import LSTM

directory_dict = {
    "reports_directory":        "../reports",
    "config_directory":         "../config",
    "graph_directory":          "../plots",
    "model_directory":          "../models",
    "tuning_directory":         "../tuning_info",
    "excel_directory":          "../excel",
    "load_run_results":         "../load_run_results",
    "current_price_directory":  "../curr_price",
    "backtest_directory":       "../backtest",
    "results_directory":        "results",
    "tax_directory":            "../tax"
}
error_file = "../error_file.txt"

test_var = "close"
time_zone = "US/EASTERN"
test_money = 10000.0
money_per_stock = 100
stocks_traded = 20
random_seed = 314
back_test_days = 100
save_logs = False
do_the_trades = True
to_plot = False
make_config = False
using_all_accuracies = False


"""
# N_STEPS = Window size or the sequence length.
# Lookup step = How many days the model will be trying to predict
# into the future.
# TEST_SIZE = How much of the data will be split between validation
# and testing. 0.2 is 20%.
# N_LAYERS = How many hidden neural layers the model will have.
# CELL = Type of cell used in each layer.
# UNITS = Number of neurons per layer.
# DROPOUT = % dropout, cells that are dropped in that training batch
# will not be used to make the output. 
# BIDIRECTIONAL = Whether or not the LSTM cells" memory can flow 
# forward in time if False or forwards and backwards in time
# LOSS = "huber_loss"
# OPTIMIZER = "adam"
# BATCH_SIZE = How many sets of data are ran together.
# EPOCHS = How many times the machine trains.
# PATIENCE = How many epochs of no improvement in the validation 
# loss it takes before the training loop is ended early.
# SAVELOAD = Whether or not to temporarily save the weights of the 
# model or to save the whole thing 
# LIMIT = how many days of data do you want 
# FEATURE_COLUMNS = what types of data do you want to include for
# your model to train on
"""

defaults = {
    "N_STEPS": 100,
    "LOOKUP_STEP": 1,
    "TEST_SIZE": 0.2,
    "N_LAYERS": 2,
    "CELL": LSTM,
    "UNITS": 256,
    "DROPOUT": 0.4,
    "BIDIRECTIONAL": False,
    "LOSS": "huber_loss",
    "OPTIMIZER": "adam",
    "BATCH_SIZE": 64,
    "EPOCHS": 800,
    "PATIENCE": 200,
    "SAVELOAD": True,
    "LIMIT": 4000,
    "FEATURE_COLUMNS": ["open", "low", "high", "close", "mid", "volume", "7_moving_avg"],
    "SAVE_FOLDER": "trading"
}


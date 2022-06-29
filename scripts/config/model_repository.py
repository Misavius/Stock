from tensorflow.keras.layers import LSTM, GRU, Dense, SimpleRNN

models = {
    "nn1" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, LSTM)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 100,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn2" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, LSTM)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn3" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, LSTM)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn4" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, LSTM)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn5" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, LSTM)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 100,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn6" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn7" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn8" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn9" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["c", "so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn10" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["7MA", "so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn11" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["pco", "pcl", "pch", "pcc", "pcm", "pcv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn12" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["c", "pco", "pcl", "pch", "pcc", "pcm", "pcv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn13" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["sc", "pcc"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn14" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "pco", "pcl", "pch", "pcc", "pcm", "pcv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn15" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, LSTM)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 100,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn16" : { 
        "N_STEPS": 300,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn17" : { 
        "N_STEPS": 50,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn18" : { 
        "N_STEPS": 20,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 100,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn19" : { 
        "N_STEPS": 150,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn20" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["pcv", "sv", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn21" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(64, LSTM), (128, Dense), (256, Dense), (256, Dense)],
        "SHUFFLE": True,
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["pcv", "sv", "tc", "vwap"],
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn22" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(64, LSTM), (128, Dense), (256, Dense), (256, Dense)],
        "SHUFFLE": True,
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn23" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": False,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn24" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.1,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "SHUFFLE": False,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "DTREE1" : {
        "FEATURE_COLUMNS": ["c"],
        "MAX_DEPTH": 10,
        "MIN_SAMP_LEAF": 1,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "RFORE1" : {
        "FEATURE_COLUMNS": ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 10,
        "MIN_SAMP_LEAF": 1,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "KNN1" : {
        "FEATURE_COLUMNS": ["c"],
        "N_NEIGHBORS": 10,
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "ADA1" : {
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 10000,
        "MIN_SAMP_LEAF": 1,
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
}

exhaustive_search = {
    "DTREE" : {
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"], ["pcv", "sv", "tc", "vwap"],
            ["sc", "pcc"], ["c", "dc", "sc", "pcc"]],
        "MAX_DEPTH": [1, 3, 5, 10, 100, 1000],
        "MIN_SAMP_LEAF": [1, 3, 5, 10],
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
    },
    "RFORE" : {
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"], ["pcv", "sv", "tc", "vwap"],
            ["sc", "pcc"], ["c", "dc", "sc", "pcc"]],
        "N_ESTIMATORS": [5, 10, 50, 100, 1000],
        "MAX_DEPTH": [1, 3, 5, 10, 100, 1000],
        "MIN_SAMP_LEAF": [1, 3, 5, 10],
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "KNN" : {
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"], ["pcv", "sv", "tc", "vwap"],
            ["sc", "pcc"], ["c", "dc", "sc", "pcc"]],
        "N_NEIGHBORS": [1, 2, 3, 4, 5, 7, 10, 20],
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
    },
    "ADA" : {
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["so", "sl", "sh", "sc", "sm", "sv", "tc", "vwap"], ["pcv", "sv", "tc", "vwap"],
            ["sc", "pcc"], ["c", "dc", "sc", "pcc"]],
        "N_ESTIMATORS": [5, 10, 50, 100, 1000],
        "MAX_DEPTH": [1, 3, 5, 10, 100, 1000],
        "MIN_SAMP_LEAF": [1, 3, 5, 10],
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
    },


}

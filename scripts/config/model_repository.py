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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["c", "s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["ma.c", "s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["c", "pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["s.c", "pc.c"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["pc.v", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["pc.v", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
        "SHUFFLE": False,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn25" : { 
        "N_STEPS": 200,
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
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn26" : { 
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
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn27" : { 
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
        "FEATURE_COLUMNS": ["wt.o", "wt.l", "wt.h", "wt.c", "wt.m", "wt.v", "wt.tc", "wt.vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn28" : { 
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
        "FEATURE_COLUMNS": ["d.o", "d.l", "d.h", "d.c", "d.m", "d.v", "d.tc", "d.vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "d.c",
        "SAVE_PRED": {}
        },
    "nn29" : { 
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
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.v", "pc.tc", "pc.vwap", "aroon_down", "aroon_up", "TSF", "ht_trendmode", "ht_sine"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn30" : { 
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
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "s.tc", "s.vwap", "day_of_week"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn31" : { 
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
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.v", "pc.tc", "pc.vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "pc.c",
        "SAVE_PRED": {}
        },
    "nn32" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, Dense), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .1,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn33" : { 
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
        "PATIENCE": 50,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn34" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 200,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn35" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 400,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn36" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 800,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn37" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 1200,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn38" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 1600,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "c",
        "SAVE_PRED": {}
        },
    "nn39" : { 
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
        "FEATURE_COLUMNS": ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "acc",
        "SAVE_PRED": {}
        },
    "nn99" : { 
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": .2,
        "LAYERS": [(256, LSTM), (256, Dense), (128, Dense), (64, Dense)],
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "binary_crossentropy",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 200,
        "PATIENCE": 200,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
        "SHUFFLE": True,
        "TEST_VAR": "acc",
        "SAVE_PRED": {}
        },
    "DTREE1" : {
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v"],
        "MAX_DEPTH": 5,
        "MIN_SAMP_LEAF": 3,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "XTREE1" : {
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 10,
        "MIN_SAMP_LEAF": 1,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "RFORE1" : {
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 10,
        "MIN_SAMP_LEAF": 1,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "KNN1" : {
        "FEATURE_COLUMNS": ["c"],
        "N_NEIGHBORS": 5,
        "WEIGHTS": "distance",
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "ADA1" : {
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 1000,
        "MIN_SAMP_LEAF": 1,
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "XGB1" : {
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 1000,
        "MAX_LEAVES": 1000,
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "BAGREG1" : {
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 1000,
        "MIN_SAMP_LEAF": 1,
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "MLP1" : { 
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
        "LAYERS": (20, 20), 
        "EARLY_STOP": True,
        "VALIDATION_FRACTION": .2,
        "PATIENCE": 5,
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c",
    },
    "MLENS1" : {
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
        "LAYERS": [["MLP1", "RFORE1"], ["ADA1", "KNN1"], ["XGB1", "BAGREG1"], ["DTREE1", "XTREE1"]],
        "META_EST": "reg",
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c",
        "DTREE1" : {
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 5,
        },
        "XTREE1" : {
            "N_ESTIMATORS": 10,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "RFORE1" : {
            "N_ESTIMATORS": 10,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "KNN1" : {
            "N_NEIGHBORS": 5,
            "WEIGHTS": "distance"
        },
        "ADA1" : {
            "N_ESTIMATORS": 100,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "XGB1" : {
                "N_ESTIMATORS": 50,
                "MAX_DEPTH": 10,
                "MAX_LEAVES": 1000,
        },
        "XGB2" : {
                "N_ESTIMATORS": 100,
                "MAX_DEPTH": 10,
                "MAX_LEAVES": 1000,
        },
        "BAGREG1" : {
            "N_ESTIMATORS": 10,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "MLP1" : { 
            "LAYERS": (10), 
            "EARLY_STOP": True,
            "VALIDATION_FRACTION": .2,
            "PATIENCE": 5,
        },
        "MLP2" : { 
            "LAYERS": (10, 10), 
            "EARLY_STOP": True,
            "VALIDATION_FRACTION": .2,
            "PATIENCE": 5,
        },
        "MLP3" : { 
            "LAYERS": (20, 10, 10), 
            "EARLY_STOP": True,
            "VALIDATION_FRACTION": .2,
            "PATIENCE": 5,
        },
    },
    "DTREE2" : {
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v"],
        "MAX_DEPTH": 5,
        "MIN_SAMP_LEAF": 3,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": "acc"
        },
    "XTREE2" : {
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 10,
        "MIN_SAMP_LEAF": 1,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": "acc"
        },
    "RFORE2" : {
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 10,
        "MIN_SAMP_LEAF": 1,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": "c"
        },
    "KNN2" : {
        "FEATURE_COLUMNS": ["c"],
        "N_NEIGHBORS": 5,
        "WEIGHTS": "distance",
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "acc"
        },
    "ADA2" : {
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 1000,
        "MIN_SAMP_LEAF": 1,
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "acc"
        },
    "XGB2" : {
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 1000,
        "MAX_LEAVES": 1000,
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "acc"
        },
    "BAGREG2" : {
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v"],
        "N_ESTIMATORS": 100,
        "MAX_DEPTH": 1000,
        "MIN_SAMP_LEAF": 1,
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "acc"
        },
    "MLP2" : { 
        "FEATURE_COLUMNS": ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"],
        "LAYERS": (20, 20), 
        "EARLY_STOP": True,
        "VALIDATION_FRACTION": .2,
        "PATIENCE": 5,
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "acc",
    },
    "MLENS2" : {
        "FEATURE_COLUMNS": ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
        "LAYERS": [["MLP1", "RFORE1"], ["ADA1", "KNN1"], ["XGB1", "BAGREG1"], ["DTREE1", "XTREE1"]],
        "META_EST": "reg",
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": "acc",
        "DTREE1" : {
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 5,
        },
        "XTREE1" : {
            "N_ESTIMATORS": 10,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "RFORE1" : {
            "N_ESTIMATORS": 10,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "KNN1" : {
            "N_NEIGHBORS": 5,
            "WEIGHTS": "distance"
        },
        "ADA1" : {
            "N_ESTIMATORS": 100,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "XGB1" : {
                "N_ESTIMATORS": 50,
                "MAX_DEPTH": 10,
                "MAX_LEAVES": 1000,
        },
        "XGB2" : {
                "N_ESTIMATORS": 100,
                "MAX_DEPTH": 10,
                "MAX_LEAVES": 1000,
        },
        "BAGREG1" : {
            "N_ESTIMATORS": 10,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "MLP1" : { 
            "LAYERS": (10), 
            "EARLY_STOP": True,
            "VALIDATION_FRACTION": .2,
            "PATIENCE": 5,
        },
        "MLP2" : { 
            "LAYERS": (10, 10), 
            "EARLY_STOP": True,
            "VALIDATION_FRACTION": .2,
            "PATIENCE": 5,
        },
        "MLP3" : { 
            "LAYERS": (20, 10, 10), 
            "EARLY_STOP": True,
            "VALIDATION_FRACTION": .2,
            "PATIENCE": 5,
        },
    },
    
}

exhaustive_search = {
    "DTREE" : { # 384
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"], ["pc.v", "s.v", "tc", "vwap"],
            ["s.c", "pc.c"], ["c", "d.c", "s.c", "pc.c"], ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"]],
        "MAX_DEPTH": [1, 3, 5, 10, 100, 1000],
        "MIN_SAMP_LEAF": [1, 3, 5, 10],
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": ["c", "acc"]
    },
    "XTREE" : { # 1920
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"], ["pc.v", "s.v", "tc", "vwap"],
            ["s.c", "pc.c"], ["c", "d.c", "s.c", "pc.c"], ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"]],
        "N_ESTIMATORS": [5, 10, 50, 100, 1000],
        "MAX_DEPTH": [1, 3, 5, 10, 100, 1000],
        "MIN_SAMP_LEAF": [1, 3, 5, 10],
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": ["c", "acc"]
        },
    "RFORE" : { # 1920
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"], ["pc.v", "s.v", "tc", "vwap"],
            ["s.c", "pc.c"], ["c", "d.c", "s.c", "pc.c"], ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"]],
        "N_ESTIMATORS": [5, 10, 50, 100, 1000],
        "MAX_DEPTH": [1, 3, 5, 10, 100, 1000],
        "MIN_SAMP_LEAF": [1, 3, 5, 10],
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": ["c", "acc"]
        },
    "KNN" : { # 160
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"], ["pc.v", "s.v", "tc", "vwap"],
            ["s.c", "pc.c"], ["c", "d.c", "s.c", "pc.c"], ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"]],
        "N_NEIGHBORS": [1, 2, 3, 4, 5, 7, 10, 20, 50, 100],
        "WEIGHTS": ["uniform", "distance"],
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": ["c", "acc"]
    },
    "ADA" : { # 1920
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"], ["pc.v", "s.v", "tc", "vwap"],
            ["s.c", "pc.c"], ["c", "d.c", "s.c", "pc.c"], ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"]],
        "N_ESTIMATORS": [5, 10, 50, 100, 1000],
        "MAX_DEPTH": [1, 3, 5, 10, 100, 1000],
        "MIN_SAMP_LEAF": [1, 3, 5, 10],
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": ["c", "acc"]
    },
    "XGB" : { # 1440
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"], ["pc.v", "s.v", "tc", "vwap"],
            ["s.c", "pc.c"], ["c", "d.c", "s.c", "pc.c"], ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"]],
        "N_ESTIMATORS": [5, 10, 50, 100, 1000],
        "MAX_DEPTH": [1, 3, 5, 10, 100, 1000],
        "MAX_LEAVES": [10, 100, 1000],
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": ["c", "acc"]
    },
    "BAGREG" : { # 1920
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"], ["pc.v", "s.v", "tc", "vwap"],
            ["s.c", "pc.c"], ["c", "d.c", "s.c", "pc.c"], ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"]],
        "N_ESTIMATORS": [5, 10, 50, 100, 1000],
        "MAX_DEPTH": [1, 3, 5, 10, 100, 1000],
        "MIN_SAMP_LEAF": [1, 3, 5, 10],
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 1,
        "TEST_VAR": ["c", "acc"]
    },
    "MLP" : { # 1408
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"], ["pc.v", "s.v", "tc", "vwap"],
            ["s.c", "pc.c"], ["c", "d.c", "s.c", "pc.c"], ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"]],
        "LAYERS": [(1), (2), (4), (8), (10), (10, 5), (20, 10, 5), (5, 10), (10, 10, 10), (50, 50), (100)],
        "EARLY_STOP": [True, False],
        "VALIDATION_FRACTION": .2,
        "PATIENCE": [3, 5, 10, 25],
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": ["c", "acc"]
        
    },
    "MLENS": { # 3712
        "FEATURE_COLUMNS": [["c"], ["o", "l", "h", "c", "m", "v"], ["o", "l", "h", "c", "m", "v", "tc", "vwap"],
            ["s.o", "s.l", "s.h", "s.c", "s.m", "s.v", "tc", "vwap"], ["pc.v", "s.v", "tc", "vwap"],
            ["s.c", "pc.c"], ["c", "d.c", "s.c", "pc.c"], ["pc.o", "pc.l", "pc.h", "pc.c", "pc.m", "pc.v", "tc", "vwap"]],
        "LAYERS": [[["DTREE1"], ["DTREE1"]], [["XTREE1"], ["XTREE1"]], [["RFORE1"], ["RFORE1"]], [["KNN1"], ["KNN1"]], 
            [["ADA1"], ["ADA1"]], [["XGB1"], ["XGB1"]], [["XGB2"], ["XGB2"]], [["BAGREG1"], ["BAGREG1"]], 
            [["MLP1"], ["MLP1"]], [["MLP2"], ["MLP2"]], [["MLP3"], ["MLP3"]], 
            [["DTREE1", "XTREE1", "RFORE1", "KNN1", "ADA1", "XGB1", "XGB2", "BAGREG1", "MLP1", "MLP2", "MLP3"]],
            [["XTREE1", "MLP2"]], [["XGB2", "ADA1"]], [["BAGREG1", "KNN1"]], [["MLP1", "MLP2", "MLP3"]], [["MLP1", "RFORE1"]], 
            [["DTREE1"]], [["XTREE1"]], [["RFORE1"]], [["KNN1"]], [["ADA1"]], [["XGB1"]], [["XGB2"]], [["BAGREG1"]], [["MLP1"]], 
            [["MLP2"]], [["MLP3"]], [["MLP1", "RFORE1"], ["ADA1", "KNN1"], ["XGB1", "BAGREG1"], ["DTREE1", "XTREE1"]]],
        "META_EST": ["reg", "SVR", "ridge", "DTREE", "RFORE", "KNN", "XGB", "MLP"],
        "LOOKUP_STEP":1,
        "TEST_SIZE": 1,
        "TEST_VAR": ["c", "acc"],
        "DTREE1" : {
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 5,
        },
        "XTREE1" : {
            "N_ESTIMATORS": 10,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "RFORE1" : {
            "N_ESTIMATORS": 10,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "KNN1" : {
            "N_NEIGHBORS": 5,
            "WEIGHTS": "distance"
        },
        "ADA1" : {
            "N_ESTIMATORS": 100,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "XGB1" : {
                "N_ESTIMATORS": 50,
                "MAX_DEPTH": 10,
                "MAX_LEAVES": 1000,
        },
        "XGB2" : {
                "N_ESTIMATORS": 100,
                "MAX_DEPTH": 10,
                "MAX_LEAVES": 1000,
        },
        "BAGREG1" : {
            "N_ESTIMATORS": 10,
            "MAX_DEPTH": 1000,
            "MIN_SAMP_LEAF": 1,
        },
        "MLP1" : { 
            "LAYERS": (10), 
            "EARLY_STOP": True,
            "VALIDATION_FRACTION": .2,
            "PATIENCE": 5,
        },
        "MLP2" : { 
            "LAYERS": (10, 10), 
            "EARLY_STOP": True,
            "VALIDATION_FRACTION": .2,
            "PATIENCE": 5,
        },
        "MLP3" : { 
            "LAYERS": (20, 10, 10), 
            "EARLY_STOP": True,
            "VALIDATION_FRACTION": .2,
            "PATIENCE": 5,
        },

    }
}

keras_tune_models = {
    "nn1": {
        "N_STEPS": 100,
        "LOOKUP_STEP": 1,
        "TEST_SIZE": 0.2,
        "LAYERS": [(256, LSTM), (256, LSTM)],
        "SHUFFLE": True,
        "DROPOUT": .4,
        "BIDIRECTIONAL": False,
        "LOSS": "huber_loss",
        "OPTIMIZER": "adam",
        "BATCH_SIZE": 1024,
        "EPOCHS": 2000,
        "PATIENCE": 200,
        "SAVELOAD": True,
        "LIMIT": 4000,
        "FEATURE_COLUMNS": ["s.c", "s.o", "s.l", "s.h", "s.m", "s.v", "s.tc", "s.vwap"],
        "TEST_VAR": "c",
        "SAVE_PRED": {},
    }


}


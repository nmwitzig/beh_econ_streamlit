from pathlib import Path
from pydoc import locate

import yaml

PIPELINE_DIR = Path(__file__).resolve().parents[1]
PARAMETERS_FILE = PIPELINE_DIR / "params.yaml"

with open(PARAMETERS_FILE) as file:
    print(f'Parsing parameters from "{PARAMETERS_FILE}"')
    params = yaml.safe_load(file)


ROOT_DIR = PIPELINE_DIR / params["root_dir"]

# Dataset parameters
RAW_DATASET_DIR = ROOT_DIR / params["data"]["download"]["subdir"]
DATASET_DIR = ROOT_DIR / params["data"]["dataset"]["subdir"]
DATASET_VAL_TEST_SPLIT = params["data"]["dataset"]["val_test_split"]


# Train parameters
BATCH_SIZE = params["train"]["batch_size"]
IMG_SIZE = tuple(params["train"]["img_size"])
LEARNING_RATE = params["train"]["learning_rate"]
TRAIN_DIR = ROOT_DIR / params["train"]["subdir"]
EPOCHS_FROZEN = params["train"]["epochs"]["frozen"]
EPOCHS_UNFROZEN = params["train"]["epochs"]["unfrozen"]
FINE_TUNE_AT = params["train"]["fine_tune_at"]


# Model parameters
BACKBONE = locate(params["model"]["backbone"])
PREPROCESS_INPUT = locate(params["model"]["preprocess_input"])


# Evaluation parameters
EVALUATION_DIR = ROOT_DIR / params["evaluate"]["subdir"]


import os

PIPELINE_NAME : str = "usvisa"
ARTIFACT_NAME : str = "artifact"
MODEL_FILE_NAME : str = "model.pkl"
FILE_NAME: str = "visa.csv"

TRAINING_FILE : str = "train.csv"
TESTING_FILE : str = "test.csv"

TARGET_COLUMN="case_status"
PREPROCESSING_FILE = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml")

DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_stores"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
 

DATA_VALIDATION_DIR_NAME : str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR : str ="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILENAME: str = "report.yaml"





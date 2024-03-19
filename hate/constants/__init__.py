import os


from datetime import datetime

ARTIFACTS_DIR: str = "artifacts"
LABEL = 'label'
TWEET = 'tweet'


"""
Data Ingestion related constant 
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://github.com/raghavpatel2507/Hate_Speech_Classification/raw/main/data/dataset.zip"


"""
Data Validation realted contant 
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["imbalanced_data.csv", "raw_data.csv"]
import os
import sys
from zipfile import ZipFile
from six.moves import urllib
from hate.logger import logging
from hate.exception import CustomException
from hate.entity.config_entity import DataIngestionConfig
from hate.entity.artifact_entity import DataIngestionArtifacts
import zipfile
class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
           raise CustomException(e, sys)
        
    

    def download_data(self)-> str:
        '''
        Fetch data from the url
        '''

        try: 
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR
            os.makedirs(zip_download_dir, exist_ok=True)
            data_file_name = os.path.basename(dataset_url)
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(f"Downloading data from {dataset_url} into file {zip_file_path}")
            urllib.request.urlretrieve(dataset_url, zip_file_path)
            logging.info(f"Downloaded data from {dataset_url} into file {zip_file_path}")
            return zip_file_path

        except Exception as e:
            raise CustomException(e, sys)
    def unzip_and_clean(self,zip_file_path: str)-> str:
        logging.info("Entered the unzip_and_clean method of Data ingestion class")
        try: 
            with ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)

            logging.info("Exited the unzip_and_clean method of Data ingestion class")

            return self.data_ingestion_config.DATA_ARTIFACTS_DIR, self.data_ingestion_config.NEW_DATA_ARTIFACTS_DIR

        except Exception as e:
            raise CustomException(e, sys) from e
    

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the initiate_data_ingestion method of Data ingestion class")

        try:
            zip_file_path = self.download_data()
            logging.info("Fetched the data from github reposetory")
            imbalance_data_file_path, raw_data_file_path = self.unzip_and_clean(zip_file_path)

            logging.info("Unzipped file and split into train and valid")

            data_ingestion_artifacts = DataIngestionArtifacts(
                imbalance_data_file_path= imbalance_data_file_path,
                raw_data_file_path = raw_data_file_path
            )

            logging.info("Exited the initiate_data_ingestion method of Data ingestion class")

            logging.info(f"Data ingestion artifact: {data_ingestion_artifacts}")

            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
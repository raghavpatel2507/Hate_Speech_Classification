import os
import io
import sys
import keras
import pickle
from PIL import Image
from hate.logger import logging
from hate.constants import *
from hate.exception import CustomException
from keras.utils import pad_sequences
from hate.components.data_transforamation import DataTransformation
from hate.entity.config_entity import DataTransformationConfig
from hate.entity.artifact_entity import DataIngestionArtifacts


class PredictionPipeline:
    def __init__(self):
        
        self.model_name = "model.h5"
        self.model_path = os.path.join("model", self.model_name)
        
        self.data_transformation = DataTransformation(data_transformation_config= DataTransformationConfig,data_ingestion_artifacts=DataIngestionArtifacts)


    
   
        

    
    def predict(self,model_path,text):
        """load image, returns cuda tensor"""
        logging.info("Running the predict function")
        try:
            
            load_model = keras.models.load_model(model_path)
            with open('tokenizer.pickle', 'rb') as handle:
                load_tokenizer = pickle.load(handle)
            
            text=self.data_transformation.concat_data_cleaning(text)
            text = [text]            
            print(text)
            seq = load_tokenizer.texts_to_sequences(text)
            padded = pad_sequences(seq, maxlen=300)
            print(seq)
            pred = load_model.predict(padded)
            pred
            print("pred", pred)
            if pred>0.5:

                print("hate and abusive")
                return "hate and abusive"
            else:
                print("no hate")
                return "no hate"
        except Exception as e:
            raise CustomException(e, sys) from e

    
    def run_pipeline(self,text):
        logging.info("Entered the run_pipeline method of PredictionPipeline class")
        try:

            
            predicted_text = self.predict(self.model_path, text)
            logging.info("Exited the run_pipeline method of PredictionPipeline class")
            return predicted_text
        except Exception as e:
            raise CustomException(e, sys) from e
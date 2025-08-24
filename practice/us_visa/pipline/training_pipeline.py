import sys 
import os  
from us_visa.exception import MyException 
from us_visa.logger import logger 
from us_visa.components.data_ingestion import DataIngestion 
from us_visa.entity.config_entity import DataIngestionConfig 
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.entity.config_entity import DataIngestionConfig 


config = DataIngestionConfig()
filepath = r"D:\desktop\AI\mlops\dswithbappy\notebook\visa.csv"

class TrainingPipeline: 
    def __init__(self): 
        self.data_ingestion_confing = DataIngestion(config,filepath)


    def initiate_data_ingestion(self): 
        logger.info("Initiate the final Data Ingestion")
        try: 
            self.data_ingestion_confing.final_method()
        except Exception as e: 
            raise MyException("Final method Error")
        

if __name__ == "__main__": 
    training = TrainingPipeline()
    training.initiate_data_ingestion()
      

from us_visa.logger import logger
from us_visa.exception import MyException
import pandas as pd

import sys
import os
from us_visa.entity.config_entity import DataIngestionConfig
from sklearn.model_selection import train_test_split

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_root not in sys.path:
    sys.path.append(project_root)

config = DataIngestionConfig()


class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig, datapath: str):
        self.datapath = datapath
        self.data_ingestion_config = data_ingestion_config

    def load_data(self) -> pd.DataFrame:
        logger.info(f"Trying to load the data from {self.datapath}")
        try:
            if not os.path.exists(self.datapath):
                raise FileNotFoundError(f"File not found: {self.datapath}")
            
            df = pd.read_csv(self.datapath)  # Fixed variable name
            logger.info(f"Data loaded successfully with shape: {df.shape}")
            return df

        except Exception as e:
            logger.error(f"Failed to load the data: {str(e)}")
            raise MyException(str(e), sys)  # Ensure MyException matches your exception class
        
    
    def export_data__into_feaature_store(self): 
        try: 
            df = self.load_data()
            logger.info(f"the Shape of the Dataframe {df.shape}")
            feature_store_filepath = self.data_ingestion_config.feature_store_filepath

            dir_path = os.path.dirname(feature_store_filepath)

            os.makedirs(dir_path,exist_ok=True)

            logger.info(f"Saving Exported Data into feature Store filepath: {feature_store_filepath}")

            return df 
        except Exception as e: 
            raise MyException("failed to export data into the feature stores")
        

    def split_data_as_train_and_test(self,df:pd.DataFrame)->None: 
        logger.info("Into the Part of Training and testing of Data")
        try: 
            train_set, test_set = train_test_split(df,test_size=self.data_ingestion_config.train_test_split_ratio)

            logger.info("Splillted Data into train and test")

            train_dir = os.path.dirname(self.data_ingestion_config.training_filepath)

            test_dir = os.path.dirname(self.data_ingestion_config.testing_filepath)

            os.makedirs(train_dir, exist_ok=True)

            os.makedirs(test_dir, exist_ok=True)

            train_set.to_csv(self.data_ingestion_config.training_filepath,index=False,header=True)

            test_set.to_csv(self.data_ingestion_config.testing_filepath,index=False,header=True)


            logger.info(f"Data split into train ({train_set.shape}) and test ({test_set.shape}) sets")


        except Exception as e: 
            raise MyException("failed to split the data")


    def final_method(self): 
        try: 
            df = self.load_data()
            self.export_data__into_feaature_store()
            self.split_data_as_train_and_test(df)
        except Exception as e: 
            raise MyException("Something Went Wrong")
        





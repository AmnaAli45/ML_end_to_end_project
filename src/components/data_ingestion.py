import os,sys
import numpy as np
import pandas as pd
from src.logger import logging
from src.exceptions import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation

@dataclass # automatically create common methods for classes that mainly store data, so you don’t have to write them manually.
class DataIngestionCoding:
    # We have three data files:
    # 1. raw data (actual data that is downloaded from cloud,database or data available locally)
    # 2. train data
    # 3. test data
    train_data_path = os.path.join("artifacts/data_ingestion","train.csv") # it will create artifacts folder and train.csv file inside it  
    test_data_path = os.path.join("artifacts/data_ingestion","test.csv") # creates test.csv file inside artifacts
    raw_data_path = os.path.join("artifacts/data_ingestion","raw.csv") # creates raw.csv file inside artifacts

class dataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionCoding()
    
    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            # reading the data
            logging.info("Data read from local system")
            data = pd.read_csv(os.path.join("notebook/data","cleandata.csv"))

            # make the directory of artifacts then save the raw data
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index = False)

            # train - test splitting of data
            logging.info("Split the data into train and test sets")
            train_set,test_set = train_test_split(data,test_size=0.2,random_state=42)

            # after splitting save data in srtifacts folder
            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)

            logging.info("Data Ingestion completed......")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info("Error occured in data ingestion phase")
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = dataIngestion()
    train_data_path ,test_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data_path ,test_data_path)

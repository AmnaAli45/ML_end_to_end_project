# Handling Missing Values
# Outliers treatment
# Handling imbalanced data
# Encoding Categorical Variables

import numpy as np
import pandas as pd
import os,sys
from src.logger import logging
from src.exceptions import CustomException
from src.utils import save_obj
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocess_obj_file_path = os.path.join("artifacts/data_transformation","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformation_obj(self):
        try:
            logging.info("Transformation Started")
            numerical_cols = ['age', 'workclass', 'educational-num', 'marital-status', 'occupation',
       'relationship', 'race', 'gender', 'capital-gain', 'capital-loss',
       'hours-per-week']
            
            num_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())])

            preprocessor = ColumnTransformer(
            [("num_pipeline",num_pipeline,numerical_cols)]) 

            return preprocessor
            
        except Exception as e:
            raise CustomException(e,sys)
    
    def remove_outliers_IQR(self,col,df):
        try:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3-Q1
            upper_limit = Q3 + 1.5*IQR
            lower_limit = Q1 - 1.5*IQR
            df.loc[(df[col]>upper_limit),col] = upper_limit 
            # selects only those rows of specific col where condition is true and replace value with upper_limit
            df.loc[(df[col]<lower_limit),col] = lower_limit
            # selects only those rows of specific col where condition is true and replace value with lower_limit
            return df
        except Exception as e:
            logging.info("Outliers Handling Code")
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            numerical_cols = ['age', 'workclass', 'educational-num', 'marital-status', 'occupation',
       'relationship', 'race', 'gender', 'capital-gain', 'capital-loss',
       'hours-per-week']
            
            for col in numerical_cols:
                self.remove_outliers_IQR(col = col,df = train_data)
            
            logging.info("Outlier Removal in train data")
            
            for col in numerical_cols:
                self.remove_outliers_IQR(col = col,df = test_data)
            
            logging.info("Outlier Removal in test data")

            preprocess_obj = self.get_data_transformation_obj()

            target_col = "income"
            drop_column = [target_col]

            logging.info("Splitting train data into dependent and independent features")

            input_feature_train_data = train_data.drop(drop_column,axis = 1)
            target_feature_train_data = train_data['income']

            logging.info("Splitting test data into dependent and independent features")

            input_feature_test_data = test_data.drop(drop_column,axis = 1)
            target_feature_test_data = test_data['income']

            logging.info("Applying transformation on train and test data")
            input_train_arr = preprocess_obj.fit_transform(input_feature_train_data)
            input_test_arr = preprocess_obj.transform(input_feature_test_data)
            
            logging.info("Applying preprocessor object  on train and test data")
            train_aar = np.c_[input_train_arr,np.array(input_feature_train_data)] # it will concatenate both of the arrays
            test_aar = np.c_[input_test_arr,np.array(input_feature_test_data)]

            save_obj(file_path=self.data_transformation_config.preprocess_obj_file_path,
                     obj=preprocess_obj)
            
            return(
                train_aar,
                test_aar,
                self.data_transformation_config.preprocess_obj_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)
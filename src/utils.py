import os,sys
from src.logger import logging
from src.exceptions import CustomException
import pickle

def save_obj(file_path , obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj: # opens the file in write mode
            pickle.dump(obj,file_obj) # This line saves your object into a file so you can load it again later.
    except Exception as e:
        raise CustomException(e,sys)
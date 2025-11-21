# We will call whole pipeline in this file
from flask import Flask
import os,sys
from src.exceptions import CustomException
from src.logger import logging # importing a custom logging setup from project

app = Flask(__name__) # Creating an instance of Flask application 
# __name__ --> tells Flask where app is located

@app.route('/',methods = ['GET','POST'])
# This defines the URL route '/', also called the home page.
# It accepts both GET and POST requests.

# ----------------- logging fuction ----------------
# def index():
#     logging.info("I am testing the logs") # message to write in logger file
#     return "end to end ML project" # message to display on web page

# ------------------- exception function -------------------
def index():
    try:
        raise Exception("I am testing Eceptions") # To manually generate an error
    except Exception  as e:
        abc = CustomException(e,sys) # passing the error to custom exception class
        logging.info(abc.error_message) # message to write in logger file
        return "End to End ML Project"


if __name__ == '__main__':
    app.run(debug=True)

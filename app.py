# We will call whole pipeline in this file
from flask import Flask
from src.logger import logging # importing a custom logging setup from project

app = Flask(__name__) # Creating an instance of Flask application 
# __name__ --> tells Flask where app is located

@app.route('/',methods = ['GET','POST'])
# This defines the URL route '/', also called the home page.
# It accepts both GET and POST requests.

def index():
    logging.info("I am testing the logs") # message to write in logger file
    return "end to end ML project" # message to display on web page

if __name__ == '__main__':
    app.run(debug=True)

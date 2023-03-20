from machinelearning.exception import  CustomException
from machinelearning.logger import logging
from flask import Flask 
import os,sys



app=Flask(__name__)

@app.route('/',methods=['GET','POST'])







def index():
    try:
        raise Exception("we are testing custom exception")
        
    except Exception as e:
        machinelearning=customexception(e,sys)
        logging.info(machinelearning.error_message)
        logging.info("we are testing logging file")

if __name__=="__main__":
    app.run(debug=True)




from flask import Flask 
from machinelearning.logger import logging
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])


def index():
    logging.info("we are just testing logging module")
    return "Hello wrld"
if __name__=="__main__":
    app.run(debug=True,port=8000)


 
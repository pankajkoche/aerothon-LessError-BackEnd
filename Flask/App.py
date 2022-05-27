from datetime import datetime
from flask_cors import CORS
from email import message
from flask import Flask,render_template
import logging as log 
log.basicConfig(level="DEBUG")

FlaskInstance = Flask(__name__)
CORS(FlaskInstance)

if __name__ == '__main__':
    log.debug("Starting the Application")
    from Api import *
    FlaskInstance.run(host="localhost",port=5000,debug=True,use_reloader=True)
     
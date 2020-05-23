#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 02:46:05 2020

@author: apple
"""


from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
pickle_in = open('RF.pickle','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def Welcome():
    return'Hello There!!!'

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])    
    if prediction==1:
        
        return "It's genuine bank note"
    else:
        return "It's not a genuine bank note"



if __name__ == '__main__':
    app.run()
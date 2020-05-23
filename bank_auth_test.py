#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 02:04:46 2020

@author: apple
"""

from flask import Flask,request
import pickle



app = Flask(__name__)
pickle_in = open('RF.pickle','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def Welcome():
    return'Hello There!!!'

@app.route('/predict')
def pred_note_auth():
    variance =request.args.get('variance')
    sqness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance,sqness,curtosis,entropy]])
    
    if prediction==1:
        
        return "It's genuine bank note"
    else:
        return "It's not a genuine bank note"



if __name__ == '__main__':
    app.run()
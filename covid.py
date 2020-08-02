# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:24:34 2020

@author: Smizzy
"""


from flask import Flask, render_template, request
import pickle
app = Flask(__name__)


@app.route('/',methods=['GET'])
def Home():
                                  return render_template('covid.html')
                                    


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
                                        from ipynb.fs.full.Covid19 import forecastmodel
                                        if request.method == 'POST':
                                                    
                                                    State=str(request.form['State'])
                                
                                                    days=int(request.form['Number of days to be predicted'])
                                                    prediction=forecastmodel(State,days)                 
                                                                                                                 
                                                    return render_template('covid.html',state="Prediction for {}".format(State),output= [prediction.to_html(classes='data')],header=True)
                                                 
        
       

if __name__=="__main__":
    app.run(debug=True)
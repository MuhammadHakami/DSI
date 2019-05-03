import flask
from flask import render_template
app = flask.Flask(__name__)

#--------  Hello Message  -----------#

@app.route('/')
def greetings():
    return """<h2>Please visit /predict to predict using the model 
    for example enter /predict?pclass=1&sex=1&age=18&fare=500&sibsp=0</h2>"""

#-------- MODEL GOES HERE -----------#

import pickle
with open('../model.pkl', 'rb') as picklefile:
    model = pickle.load(picklefile)

#-------- ROUTES GO HERE -----------#

import numpy as np
@app.route('/predict', methods=["GET"])
def predict():
    pclass = flask.request.args['pclass']
    sex = flask.request.args['sex']
    age = flask.request.args['age']
    fare = flask.request.args['fare']
    sibsp = flask.request.args['sibsp']

    item = np.array([pclass, sex, age, fare, sibsp]).reshape(1, -1)
    score = model.predict_proba(item)
    results = {'survival chances': score[0,1], 'death chances': score[0,0]}
    return flask.jsonify(results)

if __name__ == '__main__':
    '''Connects to the server'''

    HOST = '127.0.0.1'
    PORT = 5000

    app.run(HOST, PORT)
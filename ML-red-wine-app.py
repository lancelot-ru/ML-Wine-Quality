# Используя Flask, запускаем приложение на 127.0.0.1:5000

from flask import Flask, request, redirect, url_for, flash, jsonify
import pandas as pd
import pickle
import json

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
    df = pd.DataFrame(data, columns=columns) 
    df.drop(['residual sugar', 'free sulfur dioxide', 'pH'], axis=1, inplace=True)
    predictions = model.predict(df)

    if int(predictions[0]) == 1:
        prediction = 'This wine is good'
    else:
        prediction = 'This wine is bad'

    return jsonify(prediction)

if __name__ == '__main__':
    file = 'final_model.sav'
    model = pickle.load(open(file, 'rb'))
    app.run(debug=True, host='127.0.0.1')

import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template
import json

# Создание flask app:
app = Flask(__name__)

# Загрузка модели
#with open("best_model_CB1.pkl", 'rb') as pkl_file:
model = pickle.load(open("D:/IFC_Code/diploma_skillfactory/best_model_CB1.pkl", "rb"))


@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен."
    return msg

@app.route('/pereict', methods =['POST'])
def predict_func():
    features = request.json
    columns = ['status', 'propertyType', 'baths', 'fireplace', 'city', 'sqft', 'zipcode', 'state', 'Private pool', 'Built in a period', 'school rating']

    features_f = pd.DataFrame([features], columns = columns)

    predict = model.predict(features_f)
    return jsonify({'prediction': round(predict[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
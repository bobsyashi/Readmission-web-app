from flask import Flask, request, jsonify, render_template, Blueprint
import joblib
import pandas as pd

model = joblib.load('machine_learning_readmission_model_v1.pkl')

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return render_template('home-page.html')


@main.route('/predict', methods=['GET'])
def predict():
    return render_template('predict.html')


@main.route('/post-result', methods=['POST'])
def post_result():
    data = request.form
    df = pd.DataFrame([data])
    prediction = model.predict_proba(df)
    proba = prediction[0][1] * 100
    return f'Liklyhood of readmission in 30 days: {proba}'

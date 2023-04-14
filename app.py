from flask import Flask
import joblib

app = Flask(__name__)
modelo = joblib.load('modelo.joblib')

@app.route("/")
def health_check():
    return "alive"

@app.route("/predict/<longitude>/<latitude>")
def predict(longitude, latitude):
    valor_medio = modelo.predict([[longitude, latitude]])
    return f'Valor: {valor_medio.round(2)}'
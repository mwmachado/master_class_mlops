import requests

def test_alive():
    response = requests.get('http://localhost:5000')
    assert response.text == 'alive'

def test_prediction():
    url = 'http://localhost:5000/predict/-119/33'
    response = requests.get(url)
    assert response.status_code == 200 #ok
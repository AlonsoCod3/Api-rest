import os
from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

url = os.getenv("url")
token = os.getenv("TOKEN")

@app.route('/', methods=['GET'])
def index():
  return "HOLA"

# /reniec/dni?numero=46027897
@app.route('/reniec/<id>', methods=['GET'])
def dni(id):
    try:
        header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(f'{url}/reniec/dni?numero={id}', headers = header)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

# /sunat/ruc?numero=<ruc>
@app.route('/sunat/<id>', methods=['GET'])
def ruc(id):
    try:
        header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.post(f'{url}/sunat/ruc?numero={id}', headers = header)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

# /sunat/ruc/full?numero=<ruc>
@app.route('/full/sunat/<id>', methods=['GET'])
def ruc_full(id):
    try:
        header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(f'{url}/sunat/ruc/full?numero={id}', headers = header)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')

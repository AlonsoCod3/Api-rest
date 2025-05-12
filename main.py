import os
from flask import Flask, jsonify
from flask_cors import CORS
import requests
from products import get_all, get_by_id, new_product, edit_product, delete_product

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

url = os.getenv("url")
token = os.getenv("TOKEN")

@app.route('/', methods=['GET'])
def index():
  return "HOLA"

@app.route('/products')
def productos():
  return jsonify(get_all())

@app.route('/products/new')
def newo():
    nuevo = {
        "id": 1,
        "code": "0002",
        "name": "apanado",
        "description": "Plato de apanado personal",
        "price": 25.00,
        "variants": {}
    }
    return jsonify(new_product(nuevo))

@app.route('/products/new/<id>')
def newoid(id):
    return jsonify(get_by_id(id))

@app.route('/products/del/<id>')
def delo(id):
    delete_product(id)
    return jsonify(get_all())

@app.route('/products/edit/<id>')
def edito(id):
    atu = {
        "name": "cevichazo",
        "price": 10.00
    }
    edit_product(id, atu)
    return jsonify(get_all())


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
        response = requests.get(f'{url}/sunat/ruc?numero={id}', headers = header)
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

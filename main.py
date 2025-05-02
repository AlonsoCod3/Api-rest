from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return "HOLA"

@app.route('/reniec/<id>', methods=['GET'])
def get_external_data(id):
    try:
        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer apis-token-14716.UIg6Hw9Fa9d6JgOOpf1BVHQGWYyueRDj"
        }
        response = requests.get(f'https://api.apis.net.pe/v2/reniec/dni?numero={id}', headers = header)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


@app.route('/reniec/<id>', methods=['OPTIONS'])
def options():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*') # Permite todos los orígenes
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response



if __name__ == '__main__':
    app.run(host='0.0.0.0')

import os
from flask import Flask
from flask_cors import CORS
from products.routes import routing

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/')
def index():
  return "HOLA"

app.register_blueprint(routing, url_prefix="/productos")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

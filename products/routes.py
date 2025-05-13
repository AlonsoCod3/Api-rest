import os
from .get_all import get_all
from .new import new_product
from .get_by_id import get_by_id
from .edit import edit_product
from .delete import delete_product

from flask import Blueprint, jsonify, send_file
routing = Blueprint("productos", __name__)

# producto = {
#     id: number,
#     code: string, // 4 digitos
#     name: string,
#     description: string,
#     price: float,
#     variants: [
#         codigo: string; // 2 dígitos
#         nombre: string;
#         precio: number;
#     ]
# }

ruta = os.path.join(os.path.dirname(__file__), 'products.json')

@routing.route("/") #GET
def get():
    return get_all(ruta)

@routing.route("/<id>") #GET_ID
def by_id(id):
    result = get_by_id(id, ruta)

    if result:
        return jsonify(result), 200
    else:
        return jsonify({'Error':"Producto no encontrado"}), 404

@routing.route("/", methods=["POST"]) #NEW
def new():
    return new_product(ruta)


@routing.route("/<id>", methods=["PUT"]) #EDIT
def edi(id):
    return edit_product(id, ruta)

@routing.route("/<id>", methods=['DELETE']) #DELETE
def delete(id):
    return delete_product(id, ruta)

@routing.route('/download') #DOWNLOAD FILE
def descargar_productos():
    try:
        return send_file(
            ruta,           # Ruta al archivo
            as_attachment=True,         # Fuerza la descarga
            download_name='productos.json',  # Nombre del archivo al descargar
            mimetype='application/json' # Tipo MIME
        )
    except FileNotFoundError:
        return {"error": "Archivo no encontrado"}, 404
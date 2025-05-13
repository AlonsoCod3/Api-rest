from .new import add
from .get_all import get_all
from flask import request, jsonify

# Función para eliminar un producto por id
def delete_product(id, ruta):
    productos = get_all(ruta)

    producto = next((p for p in productos if p["id"] == id), None)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    productos_filtrados = [producto for producto in productos if producto['id'] != id]
    
    result_delete = add(productos_filtrados, ruta)

    if not result_delete:
        return jsonify({"Error": "No se pudo borrar el producto"}), 500

    return jsonify({"mensaje": f"Producto con ID '{id}' eliminado"}), 200


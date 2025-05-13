# Función para añadir un producto
from flask import request, jsonify
import json
from .get_all import get_all
import uuid

num_products = 0

def new_product(ruta):

    data = request.get_json()
    if not data:
        return jsonify({"Error": "JSON inválido o ausente"}), 400
    
    errores = validar_producto(data)
    if errores:
        return jsonify({"Errores": errores}), 400

    new_arr = append_item(data, ruta)

    print("Resultado de arreglo", new_arr)
    if not new_arr:
        return jsonify({"error": "Ya existe un producto con ese Nombre"}), 400

    result = add(new_arr, ruta)

    if not result:
        return jsonify({"mensaje": "Ocurrio un error creando el producto", "producto" : data["name"]}), 500

    return jsonify({"mensaje": "Producto creado", "producto": data["name"]}), 200

def add(item, ruta):
    try:
        with open(ruta, 'w') as archivo:
            json.dump(item, archivo, indent=4)

        return True
    except Exception as e:
        # Captura cualquier otro error general
        print(f"Error inesperado: {e}")
        return False
    

def append_item(item, ruta):
    productos = get_all(ruta)
    global num_products
    num_products = len(productos)

    if any(p["name"] == item["name"].lower() for p in productos):
        return False
    
    product = generate_data(item)
    productos.append(product)

    return productos


def generate_data(item):
    result = {}

    result["id"] = str(uuid.uuid4())
    result["code"] = str(num_products).zfill(3)
    result["name"] = item["name"].lower()
    result["description"] = item["description"].lower()
    result["price"] = item["price"]
    result["variants"] = []
    if item.get("variants"):
        for i in item["variants"]:
            variant = {}
            variant["code"] = str(len(result["variants"])).zfill(3)
            variant["name"] = i["name"].lower()
            variant["price"] = i["price"]
            result["variants"].append(variant)
    
    print("GEnerador: ", result)
    return result


# Función de validación
def validar_producto(item):
    errores = []

    if not isinstance(item.get("name"), str):
        return ("El 'name' debe ser una cadena")

    if not isinstance(item.get("description"), str):
        return ("El 'description' debe ser una cadena")

    if not isinstance(item.get("price"), (int, float)):
        return ("El 'price' debe ser un número")

    # Validar variants
    if item.get("variants"):
        variants = item.get("variants")

        if not isinstance(variants, list):
            return ("El 'variants' debe ser una lista")
        else:
            for i, variant in enumerate(variants):
                
                if not isinstance(variant.get("name"), str):
                    return (f"Variant[{i}]: 'nombre' debe ser una cadena")
                if not isinstance(variant.get("price"), (int, float)):
                    return (f"Variant[{i}]: 'precio' debe ser un número")
    else:
        print("not hay")
    return False
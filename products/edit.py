from .new import add
from .get_all import get_all
from flask import request, jsonify

# Función para editar un producto existente
def edit_product(id, ruta):
    data = request.get_json()

    productos = get_all(ruta)

    producto = next((p for p in productos if p["id"] == id), None)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    
    result_validate = validar_producto(data)

    if result_validate:
        return jsonify({"Error":result_validate}), 500

    # Actualizar datos para no borrar datos requeridos
    result_to_update = generate_update(data)

    # Actualizar solo los campos enviados
    for key in result_to_update:
        if key in producto:
            producto[key] = data[key]
    
    result_edit = add(productos, ruta)

    if not result_edit:
        return jsonify({"Error": "No se pudo editar el producto"}), 500

    return jsonify({
        "mensaje": "Producto actualizado correctamente",
        "producto": producto
    }), 200


def generate_update(item):
    result = item
    print(f"PRODUCTO: {item} \n")

    id_item = result.pop("id", None)
    code_item = result.pop("code", None)

    if result.get("variants"):
        for i in result["variants"]:
            code_item_variable = i.pop("code",None)
    
    return result


# Función de validación
def validar_producto(data):
    errores = []

    if data.get("name"):
        if not isinstance(data.get("name"), str):
            return ("El 'name' debe ser una cadena")

    if data.get("description"):
        if not isinstance(data.get("description"), str):
            return ("El 'description' debe ser una cadena")

    if data.get("price"):
        if not isinstance(data.get("price"), (int, float)):
            return ("El 'price' debe ser un número")

    # Validar variants
    if data.get("variants"):
        variants = data.get("variants")

        if not isinstance(variants, list):
            return ("El 'variants' debe ser una lista")
        else:
            for i, variant in enumerate(variants):
                if not variant.get("code"):
                    return (f"Variant[{i}]: 'code' no incluido")

                if variant.get("name"):
                    if not isinstance(variant.get("name"), str):
                        return (f"Variant[{i}]: 'nombre' debe ser una cadena")

                if variant.get("price"):
                    if not isinstance(variant.get("price"), (int, float)):
                        return (f"Variant[{i}]: 'precio' debe ser un número")

    return False
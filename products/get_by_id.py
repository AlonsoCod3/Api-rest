from .get_all import get_all

def get_by_id(id,ruta):
    productos = get_all(ruta)

    producto = next((p for p in productos if p["id"] == id), None)

    return producto

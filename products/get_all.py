import json

sizes = [10,20,50,100] #tamaños para paginacion

def get_all(ruta):
    with open(ruta, 'r') as archivo:
        # Cargar el contenido del archivo JSON
        products = json.load(archivo)
    return products
import json
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
ruta = "products.json"

def get_all():
    with open(ruta, 'r') as archivo:
        # Cargar el contenido del archivo JSON
        products = json.load(archivo)
    return products

def add(productos):
    with open(ruta, 'w') as archivo:
        json.dump(productos, archivo, indent=4)

def get_by_id(id):
    productos = get_all()
    for producto in productos:
        if producto['code'] == id:
            return producto
    return None

# Función para añadir un producto
def new_product(nuevo_producto):
    productos = get_all()
    productos.append(nuevo_producto)
    add(productos)
    return get_all()

# Función para eliminar un producto por código
def delete_product(codigo):
    productos = get_all()
    productos_filtrados = [producto for producto in productos if producto['code'] != codigo]
    add(productos_filtrados)

# Función para editar un producto existente
def edit_product(codigo, datos_actualizados):
    productos = get_all()
    for i, producto in enumerate(productos):
        if producto['code'] == codigo:
            productos[i].update(datos_actualizados)
            add(productos)
            return True
    return False
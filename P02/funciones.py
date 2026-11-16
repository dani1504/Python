import requests
URL_PRODUCTOS = "https://dummyjson.com/products"

def obtener_productos(limite=10):
    """Consulta DummyJSON y devuelve la lista 'products'.

    Propaga RequestException si falla HTTP o la conexión y ValueError si
    la respuesta no contiene la estructura esperada.
    """
    if not isinstance(limite, int) or isinstance(limite, bool) or limite <= 0:
        raise ValueError("El límite debe ser un entero positivo")

    respuesta = requests.get(
        URL_PRODUCTOS,
        params={"limit": limite},
        timeout=10,
    )
    respuesta.raise_for_status() #  Si servidor devuelve error lanza excepción HTTPError
    datos = respuesta.json()

    if not isinstance(datos, dict) or not isinstance(datos.get("products"), list):
        raise ValueError("Respuesta inesperada: falta la lista 'products'")

    return datos["products"]

def mostrar_productos(productos):
    lista = obtener_productos()
    print("-"*80)
    print(f"{"ID":<5}{"PRODUCTO":<30}{"CATEGORIA":<15}{"PRECIO":<15}{"STOCK":<15}")
    print("-"*80)
    for x in productos:
        print(f"{x["id"]:<5}{x["title"]:<30}{x["category"]:<15}{x["price"]:<15}{x["stock"]:<15}")

def buscar_por_titulo(productos, texto):
    return [x for x in productos if texto.lower() == x["title"].lower()]


def filtrar_productos(productos, categoria=None, precio_max=None, solo_disponibles=False):
    for x in productos:
        if x["category"].lower() == categoria and x["price"] == precio_max and x["stock"] == solo_disponibles:
            return x
    return None
        
        

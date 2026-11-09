# from servidores import SERVIDORES, LISTAUNO, LISTAVACIA # Esto lo que hace es cojer las variables definidas en otro archivo y definirlas en este archivo.

# APARTADO01:

def mostrar_inventario(servidores):
    """Muestra la información básica de los servidores recibidos."""
    if servidores:
        print("-"*70)
        print(f"{'ID':<5}{'NOMBRE':<12}{'ROL':<16}{'ESTADO':<12}{'CPU':<5}{'RAM'}")
        print("-"*70)
        for servidor in servidores:
            cpu_texto = f"{servidor['cpu']}%"
            ram_texto = f"{servidor['ram']}%"
            print(f"{servidor['id']:<5}{servidor['nombre']:<12}{servidor['rol']:<16}{servidor['estado']:<12}{cpu_texto:<5}{ram_texto}")
    else:
        print("La lista esta  vacia")
   
#mostrar_inventario(SERVIDORES)
# APARTADO02:

def buscar_por_id(servidores, identificador):
    """Devuelve el diccionario correspondiente o None si no existe."""  
    for servidor in servidores:
        if servidor['id'] == identificador:
            return servidor
    return None

"""resultado = buscar_por_id(SERVIDORES, 101)"""

"""if resultado:
    mostrar_inventario([resultado])
else:
    print("No se encontro ningun servidor con ese ID")"""

# APARTADO03

def filtrar_por_estado(servidores, estado):
    """Devuelve una lista con los servidores del estado indicado."""
    lista_estado = []
    for servidor in servidores:
        if servidor['estado'] == estado:
            lista_estado.append(servidor)
    return lista_estado

    # OTRA FORMA DE HACERLO::(mas pro mas nota)
    # return[x for x in servidores if x['estado'] == estado]


def filtrar_por_rol(servidores, rol):
    """Devuelve una lista con los servidores del rol indicado."""
    lista_rol = []
    for servidor in servidores:
        if servidor['rol'] == rol:
            lista_rol.append(servidor)
    return lista_rol

# APARTADO04

# def calcular_resumen(servidores):
#     """Devuelve un diccionario con las estadísticas globales."""
#     lista_encendidos = filtrar_por_estado(servidores, "encendido")
    
#     total = len(servidores)
#     encendidos = len(lista_encendidos)
#     apagados = total - encendidos
    
#     if total == 0:
#         disponibilidad = 0.0
#     else:
#         disponibilidad = (encendidos / total) * 100

#     resumen = {
#         "total": total,
#         "encendidos": encendidos,
#         "apagados": apagados,
#         "disponibilidad": disponibilidad
#     }
#     return resumen

# def mostrar_resumen(servidores):
#     """Presenta las estadísticas de forma legible."""
#     resumen = calcular_resumen(servidores)

#     print(f"Total: {resumen['total']}") 
#     print(f"Encendidos: {resumen['encendidos']}") 
#     print(f"Apagados: {resumen['apagados']}") 
#     print(f"Disponibilidad: {resumen['disponibilidad']:.2f}%")

"""mostrar_resumen(SERVIDORES)"""
"""mostrar_resumen([])"""

# APARTADO05 

def calcular_resumen(servidores):
    """Devuelve un diccionario con las estadísticas globales."""
    lista_encendidos = filtrar_por_estado(servidores, "encendido")
    total = len(servidores)
    encendidos = len(lista_encendidos)
    apagados = total - encendidos
    if total == 0:
        disponibilidad = 0.0
    else:
        disponibilidad = (encendidos / total) * 100

    # Sin hacer todavia porque no lo entiendo
    suma= 0
    for x in lista_encendidos:
        suma = suma + x["cpu"]

    cpu_media = suma / encendidos

    suma_ram = 0
    for x in lista_encendidos:
        suma_ram += x["ram"]

    ram_media = suma_ram / encendidos

    resumen = {
        "total": total,
        "encendidos": encendidos,
        "apagados": apagados,
        "disponibilidad": disponibilidad,
        "cpu_media": cpu_media,
        "ram_media": ram_media
    }
    return resumen

def mostrar_resumen(servidores):
    """Presenta las estadísticas de forma legible."""
    resumen = calcular_resumen(servidores)

    print(f"Total: {resumen['total']}") 
    print(f"Encendidos: {resumen['encendidos']}") 
    print(f"Apagados: {resumen['apagados']}") 
    print(f"Disponibilidad: {resumen['disponibilidad']:.2f}%")
    print(f"CPU media: {resumen['cpu_media']:.2f}%")
    print(f"RAM media: {resumen['ram_media']:.2f}%")

# mostrar_resumen(SERVIDORES)

#APARTADO06 

def mostrar_servicios(servidor):
    """Muestra los servicios y su estado en un servidor."""
    print("Servidor:", servidor["nombre"])
    for x in servidor["servicios"]:
        print(x,":", servidor["servicios"][x])

def mostrar_servicios_empresa(s):
    """Muestra los servicios y su estado de todos los servidores."""
    for x in s:
        print("-"*20)
        mostrar_servicios(x)
    print("-"*20)

def contar_servicios_inactivos(servidores):
    """Cuenta servicios inactivos en servidores encendidos. y lo devuelve comoo resultado"""
    encendidos = filtrar_por_estado(servidores, "encendido")
    
    contador= 0
    for servidor in encendidos:
        for x in servidor["servicios"]:
            if servidor["servicios"][x] == "inactivo":
                contador = contador + 1
    return contador


#APARTADO07



if __name__ == '__main__':
    print("Solo se imprime si se invoca el modulo") # Esto se pone para hacer tests de los codigos.
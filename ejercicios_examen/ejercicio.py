from servidores import SERVIDORES, LISTAUNO

def mostrar_inventario(servidores):
    """Muestra la información básica de los servidores recibidos."""

def filtrar_por_estado(servidores, estado):
    """Devuelve una lista con los servidores del estado indicado."""
    lista = []

    for x in servidores:
        if x[estado] == estado:
            lista.append(servidor)

    return lista


servidores_encendidos = filtrar_por_estado(SERVIDORES, "encendido")
mostrar_inventario(servidores_encendidos)
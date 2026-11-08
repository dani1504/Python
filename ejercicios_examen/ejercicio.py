from servidores import SERVIDORES, LISTAUNO, LISTAVACIA # Esto lo que hace es cojer las variables definidas en otro archivo y definirlas en este archivo.

# print(SERVIDORES)


# def mostrar_inventario(servidores):
#     """Muestra la información básica de los servidores recibidos."""

# def filtrar_por_estado(servidores, estado):
#     """Devuelve una lista con los servidores del estado indicado."""
#     lista = []

#     for x in servidores:
#         if x[estado] == estado:
#             lista.append(servidor)

#     return lista


# servidores_encendidos = filtrar_por_estado(SERVIDORES, "encendido")
# mostrar_inventario(servidores_encendidos)

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
        print("La lista esta vacia")
        

mostrar_inventario(SERVIDORES)
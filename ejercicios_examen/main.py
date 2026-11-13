# ejercicios.py

from servidores import SERVIDORES, LISTAUNO, LISTAVACIA
import funciones as f

# lista_encendidos = f.filtrar_por_estado(SERVIDORES, "encendido")
# f.mostrar_inventario(lista_encendidos)

# lista_apagados = f.filtrar_por_estado(SERVIDORES, "apagado")
# f.mostrar_inventario(lista_apagados)

# res = f.calcular_resumen(SERVIDORES)
# f.mostrar_servicios_empresa(SERVIDORES)

# res = f.contar_servicios_inactivos(SERVIDORES)
# print(res)

try:
    f.cambiar_estado(SERVIDORES, 103, "down")
except ValueError:
    print("Estado no")


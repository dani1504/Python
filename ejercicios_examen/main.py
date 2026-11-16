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

"""try:
    f.cambiar_estado(SERVIDORES, 103, "down")
except ValueError:
    print("Estado no")"""


print("=== CONSOLA DE INVENTARIO LINUX ===")
print("1. Ver inventario \n2. Buscar servidor por ID \n3. Filtrar por rol\n4. Resumen de la infraestructura\n5. Ver servicios de un servidor\n6. Cambiar estado de un servidor\n7. Cambiar estado de un servicio\n0. Salir")
opcion = int(input("Elige una opcion: "))
match opcion:
    case 1:
        print("Has elegido la opcion 1")
        f.mostrar_inventario(SERVIDORES)
    case 2:
        print("Has elegido la opcion 2")
        id = int(input("Ingresa el id del servidor: "))
        servidor = [f.buscar_por_id(SERVIDORES, id)]
        if servidor:
            f.mostrar_inventario(servidor)
        else:
            print("No se encontro ningun servidor con ese ID")
    case 3:
        print("Has elegido la opcion 3")
        rol = input("Ingrese el rol del servidor: ")
        servidor = f.filtrar_por_rol(SERVIDORES, rol)
        if rol:
            f.mostrar_inventario(servidor)
        else:
            print("No se encontro ningun servidor con ese rol")
    case 4:
        print("Has elegido la opcion 4")
        f.mostrar_resumen(SERVIDORES)
    case 5:
        print("Has elegido la opcion 5")
        numero = int(input("Ingresa el numero del servidor: "))
        f.mostrar_servicios(SERVIDORES[numero])
    case 6:
        print("Has elegido la opcion 6")
    case 7:
        print("Has elegido la opcion 7")
    case 8:
        print("Has elegido la opcion 8")
    case 0:
        print("Saliendo de la consola...")
    case _:
        print("No ha indicado ninguna opcion contemplada")
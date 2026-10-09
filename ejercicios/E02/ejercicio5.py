opcion = int(input("Elige una opcion: "))

match opcion:
    case 1:
        print("Has elegido la opcion 1")
        print("Crear usuario")
    case 2:
        print("Has elegido la opcion 2")
        print("Eliminar usuario")
    case 3:
        print("Has elegido la opcion 3")
        print("Salir")
    case _:
        print("No has elegido ninguna opcion")
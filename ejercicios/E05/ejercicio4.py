equipo = {
    "hostname": "server01",
    "ip": "192.168.1.10",
    "so": "Linux"
}

clave = input("Introduce el nombre de una clave: ")

if clave in equipo:
    print(equipo[clave])
else:
    print("Esa clave no existe en el diccionario.")
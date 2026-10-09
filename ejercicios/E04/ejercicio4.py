ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]

ip = input("Ingrese una ip: ")

if ip in ips:
    posicion = ips.index(ip)
    print("La ip esta en la lista, en la posicion,", posicion)
else:
    print("La ip no esta en la lista")


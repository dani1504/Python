ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]\

ip = input("Ingrese una ip: ")

if ip in ips:
    print("La ip esta en la lista")
else:
    print("La ip no esta en la lista")
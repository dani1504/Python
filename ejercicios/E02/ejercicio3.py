edad = int(input("Ingrese tu edad: "))
saldo = int(input("Ingrese su saldo: "))

if edad >= 18 and saldo > 0:
    print("Tiene acceso al sistema")
else:
    print("No tiene acceso")
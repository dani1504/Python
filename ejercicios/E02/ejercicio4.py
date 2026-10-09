numeroa = int(input("Ingrese un numero entero: "))
numerob = int(input("Ingrese otro numero entero: "))

if numeroa > numerob:
    print(numeroa, "es mayor que", numerob)
elif numerob > numeroa:
    print(numerob, "es mayor que", numeroa)
else:
    print("Los numeros son iguales")
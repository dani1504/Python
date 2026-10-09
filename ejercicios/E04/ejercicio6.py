nombres = input("Ingresa los nombres separados por comas: ")

lista_nombres = nombres.split(",")
print(lista_nombres)

for x in range(len(lista_nombres)):
    print(lista_nombres[x])

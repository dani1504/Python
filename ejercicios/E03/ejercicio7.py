palabra = input("Ingrese una palabra: ")

print("Palabra:", palabra)
for x in range(len(palabra)):
    caracter = palabra[x]
    print(x,":", caracter)
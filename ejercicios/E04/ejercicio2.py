usuarios = ["ana", "luis", "marta"]

# usuarios[0] = "alfredo"
# usuarios.append("raquel")
# usuarios.insert(1, "carlos")

# print(usuarios)

# imagina que no sé dónde está ana

if "ana" in usuarios:
    posicion = usuarios.index("ana")
    print("ana esta en la lista además en la posicion,", posicion)
else:
    print("ana no esta en la lista")

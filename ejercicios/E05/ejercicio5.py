puertos = {
    "ssh": 22,
    "http": 80,
    "https": 443
}

for clave, valor in puertos.items():
    print(clave, "=>", valor)
import funciones as f

productos = f.obtener_productos()
# print(productos)

# f.mostrar_productos(productos)

# titulo = f.buscar_por_titulo(productos, "powder        ")
# f.mostrar_productos(titulo)

# filtro = f.filtrar_productos(productos, "fragrances", 49.99, 13)
# f.mostrar_productos(filtro)

ejercicio3 = f.filtrar_productos (productos, None, None, True)
f.mostrar_productos(ejercicio3)
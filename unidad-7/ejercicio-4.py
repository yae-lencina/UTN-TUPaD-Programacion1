#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.


productos = []   # lista donde guardaremos los diccionarios

buscar=input("ingrese: ")

with open("productos.txt", "r") as archivo:
    for linea in archivo:

        linea = linea.strip()    # saco espacios y \n

        if linea == "":
            continue    # si está vacía, la salto

        # separo la línea por comas
        nombre, precio, cantidad = linea.split(",")

        # creo el diccionario para este producto
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        # agrego el diccionario a la lista
        productos.append(producto)

# Mostrar la lista completa
print(productos)


if buscar in productos:
    print("encontrado")
    print(productos[buscar])
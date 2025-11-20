#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.
productos=[]

buscar=input("Ingrese nombre del producto: ")

with open ("productos.txt","r") as archivo:
    for linea in archivo:
        linea=linea.strip()

        if linea == "":
            continue
    
        nombre, precio, cantidad= linea.split(",")
        producto={
            "nombre: ":nombre,
            "precio: ":precio,
            "cantidad: ":cantidad
        }

        productos.append(producto)

if buscar in productos:
    if productos[nombre] == buscar:
        print(productos[buscar])

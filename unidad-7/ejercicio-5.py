#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.
productos=[]

buscar=input("Ingrese nombre del producto: ")

encontrado=False

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
    
for i in productos:
    if i["nombre: "].lower()==buscar.lower():
        encontrado=True
        print(i)

if encontrado==False:
    print("EROR.Producto no encontado.")




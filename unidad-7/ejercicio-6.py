#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista

productos = []

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea == "":
            continue

        nombre, precio, cantidad = linea.split(",")

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        productos.append(producto)



buscar = input("Ingrese nombre del producto a buscar: ")


for i in productos:
    if i["nombre"].lower()==buscar.lower():
        encontrado=True
        print(i)

if encontrado==False:
    print("EROR.Producto no encontado.")
      



agregar = input("\n¿Desea agregar un producto nuevo? (s/n): ").lower()

if agregar == "s":
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")

    nuevo = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(nuevo)
    print("\n Producto agregado correctamente.")


with open("productos.txt", "w", encoding="utf-8") as archivo:
    for i in productos:
        linea = f"{i['nombre']},{i['precio']},{i['cantidad']}\n"
        archivo.write(linea)

print("\n Archivo actualizado correctamente.")

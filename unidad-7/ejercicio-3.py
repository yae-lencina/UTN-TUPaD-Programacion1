#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente

with open ("productos.txt","a") as archivo:
    archivo.write("\nanotador,$50,100")
    print(archivo)
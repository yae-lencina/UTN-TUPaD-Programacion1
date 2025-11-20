#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

print("1. Escribiendo archivo")
archivo_productos = open("productos.txt", "w")
archivo_productos.write("Lapicera,$20,50")
archivo_productos.write("\nCuaderno,$20,$12")
archivo_productos.write("\nGoma,$4,20")
archivo_productos.close()       
#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

stock={'alfajor' : 200, 'turron':50, 'gaseosa': 150}

producto=input("/nIngrese nombre del producto a consutar: ")

if producto in stock:
    print("/nLa cantidad en nuestro stock del ",producto," es: ", stock[producto])
else:
    stock
    print("/nEl producto no se encuentra.")
    cantidad=input("Para agregarlo a nuestro stock.Ingrese cantidad del nuevo producto.: ")
    stock[producto]=cantidad

print("/nStock completo: ", stock)
import string
nombre=input("ingrese su nombre: ")
opcion=int(input("Elija una opcion : \n1.Todo en mayuscula.\n2.Todo minuscula.\n3.Solo inicial\n"))

if (opcion== 1):
    modificado=nombre.lower()
    print(modificado)
elif (opcion == 2):
    modificado=nombre.upper()
    print(modificado)
elif (opcion == 3):
    modificado=nombre.title()
    print(modificado)
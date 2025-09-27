estudiantes=["juan","pedro","felipe","marta","luciano"]

print("Listado de presentes: ",estudiantes)
opcion=input("1.Agregar un estudiante \n2.Borar un estudiante\n")
if (opcion=="1"):
    nombre=input("Ingrese nombre del nuevo estudiante: ")
    estudiantes.append(nombre)
elif (opcion=="2"):
 nombre=input("Cual estudiante desea eliminar? ")
 if(nombre in estudiantes):
    estudiantes.remove(nombre)


print(estudiantes)
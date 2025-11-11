#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda={}

for i in range (3):
    nombre=input("\nIngese nombre: ")
    numero=input("Ingrese numero: ")
    agenda[nombre]=numero

buscar=input("\nIngrese contacto para buscar: ")

if buscar in agenda:
   print("El numero de ",buscar,"es: ",agenda[buscar])
else:
   print("El nombre ingresado no existe en nuestros registros.")

#print(agenda)
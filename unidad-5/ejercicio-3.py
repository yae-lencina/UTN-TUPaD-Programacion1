#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.


def informacion_personal (a,b,c,d):
    return print("Soy ",a," ",b," tengo ",c," años de edad y vivo en ", d)

nombre=input("ingrese su nombre: ")
apellido=input("\ningrese su apellido: ")
edad=input("\nIngrese su edad: ")
lugar=input("\nIngrese su residencia: \n")

informacion_personal(nombre,apellido,edad,lugar)

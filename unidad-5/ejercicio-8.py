#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(a,b):
    imc = a/(b**2)
    return round (imc,2)

peso=int(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su alturqa en m: "))
print("Su indice de masa corporal es: ",calcular_imc(peso,altura))
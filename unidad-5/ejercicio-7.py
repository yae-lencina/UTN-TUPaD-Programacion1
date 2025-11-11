#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.


def operaciones_basicas (a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a//b
    return print("resultados suma:",suma," resta: ", resta," multiplicacion: ", multiplicacion, " division: ", division)

num1=int(input("Ingrese dos numero para realizar las operaciones basicas: "))
num2=int(input("Ingrese otro numero: "))
operaciones_basicas(num1,num2)
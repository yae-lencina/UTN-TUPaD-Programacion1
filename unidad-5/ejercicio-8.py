def calcular_imc(a,b):
    imc = a/(b**2)
    return round (imc,2)

peso=int(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su alturqa en m: "))
print("Su indice de masa corporal es: ",calcular_imc(peso,altura))
positivo=0
negativo=0
par=0
impar=0
for i in range (0,10,+1):
    numero=int(input("Ingrese numero: "))
    if(numero%2 == 0):
        par=par+1
        if(numero>0):
         positivo =positivo+1
        else:
         negativo =negativo+1
    else:
        impar=impar+1
        if(numero>0):
             positivo =positivo+1
        else:
             negativo =negativo+1


print("Cantidad de numeros positivos: ", positivo)
print("Cantidad de numeros negativos: ", negativo)
print("Cantidad de numeros pares: ", par)
print("Cantidad de numeros impares: ", impar)

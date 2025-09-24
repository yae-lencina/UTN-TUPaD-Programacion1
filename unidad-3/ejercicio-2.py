numero=int(input("Ingrese un numero: "))
contador=0
while numero >1 :
    numero=numero/10
    contador=contador + 1
print("El numero ingresado tiene ", contador, " digitos. ")
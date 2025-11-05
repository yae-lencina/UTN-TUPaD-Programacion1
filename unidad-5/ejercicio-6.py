def tabla (x):
    for i in range(1,11):
        mult=i*x
        print(x,"X",i,"=",mult)

numero=int(input("Ingrese un numer: "))
tabla(numero)
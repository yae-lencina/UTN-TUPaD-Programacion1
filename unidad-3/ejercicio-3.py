numero=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese otro numero: "))

if (numero<numero2):
    sumatoria=0
    for i in range (numero+1,numero2):
        print(sumatoria)
        sumatoria = sumatoria+i
        

print("La sumatoria entre los numeros ", numero,  " y ", numero2 , " es: ", sumatoria)

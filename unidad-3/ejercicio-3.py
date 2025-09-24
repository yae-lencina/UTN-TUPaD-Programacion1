numero=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese otro numero: "))

if (numero<numero2):
    sumatoria=numero
    for i in range (numero+1,numero2 +1):
        print(sumatoria)
        sumatoria = sumatoria+i
        #print(sumatoria)
#sumatoria= sumatoria+numero2

print("La sumatoria entre los numeros ", numero,  " y ", numero2 , " es: ", sumatoria)

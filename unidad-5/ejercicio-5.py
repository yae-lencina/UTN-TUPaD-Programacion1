def segundos_a_horas(n):
    horas=n//3600
    min=n%3600
    return horas, min

segundos=int(input("Ingrese segundos: "))
print("Son: ",segundos_a_horas(segundos), " horas y ", min, "minutos")
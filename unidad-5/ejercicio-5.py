#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(n):
    horas=n//3600
    return horas

segundos=int(input("Ingrese segundos: "))
print("Son: ",segundos_a_horas(segundos), " horas")
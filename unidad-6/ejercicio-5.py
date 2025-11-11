#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

mi_set=set()
frase=input("\n Ingrese frase para el diccionario: \n")
palabras=frase.split()
mi_set=set(palabras)

for i in palabras:
    contador=0

    if i not in mi_set:
        contador=1
    else:
        contador = contador+ 1

    print (i,":",contador)

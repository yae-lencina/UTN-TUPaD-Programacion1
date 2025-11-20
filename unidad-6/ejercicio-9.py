#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.


original={'argentina':'bs as', 'chile':'Santiago de chile', 'Bolivia': 'La paz', 'Paraguay':'Asuncion'}
invertido={}

for i in original:
    key=original[i]
    invertido[key]=i

print(invertido)

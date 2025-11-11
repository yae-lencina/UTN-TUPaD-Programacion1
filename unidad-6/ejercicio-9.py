original={'argentina':'bs as', 'chile':'Santiago de chile', 'Bolivia': 'La paz', 'Paraguay':'Asuncion'}
invertido={}

for i in original:
    key=original[i]
    invertido[key]=i

print(invertido)

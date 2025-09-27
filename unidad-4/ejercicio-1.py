notas=[10,5,6,1,7,8,6,5,7,8]
sumatoria=0
max=0
min=notas[0]
for i in notas:
    sumatoria+= i
    if (i>max):
        max=i
    elif(i<min):
        min=i

promedio=sumatoria/10
print("Las notas son: ",notas)
print("El promedio es: ",promedio)
print("La nota mas alta es: ",max)
print("La nota mas baja es: ",min)
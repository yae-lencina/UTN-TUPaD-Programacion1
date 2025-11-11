#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
tupla=()
diccionario={}
promedios={}
sumatoria=0
for a in range (3):
 nombre=input("\nIngrese nombre del alumno: ")
 tupla=()
 for i in range(3):
     nota=int(input("Ingrese nota: "))
     sumatoria=sumatoria+nota
     nuevo=(nota,)
     tupla=tupla + nuevo
 promedio=sumatoria/3
 diccionario[nombre]=tupla
 promedios[nombre]=promedio
 print(diccionario)
 
print("Los promedios son los siguientes: ",promedios)
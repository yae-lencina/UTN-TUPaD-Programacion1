import random

aleatorio = random.randint(1, 10)  
print(aleatorio) 
intentos=1

numero = int(input("Adivina el número: "))

while numero != aleatorio:
      numero = int(input("Incorrecto. Reingrese número: "))
      intentos = intentos + 1

print("\n Correcto. Adivinó el numero. Intentos: ", intentos)
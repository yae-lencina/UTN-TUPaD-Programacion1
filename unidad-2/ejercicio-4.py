edad=int(input("Ingrese su edad: "))

if(edad<12):
    print("Niño")
elif((edad>=12) and (edad<18)):
    print("Adolescente.")
elif((edad>=18) and (edad<30)):
    print("Adulto joven.")
else:
    print("Adulto.")
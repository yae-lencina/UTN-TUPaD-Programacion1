
palabra=input("ingrese una palabra ")
letra=palabra[-1]

print (letra)

if(letra in "aeiou" ):
    print (palabra + "!")
else:
    print (palabra)
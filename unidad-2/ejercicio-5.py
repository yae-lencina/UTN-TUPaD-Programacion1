clave=input("ingrese contraseña entre 8 y 14 caracteres: ")

if (len(clave)>=8) and (len(clave)<15):
    print("Contraseña correcta.")
else:
    print("Por favor. Reingrese contraseña entre 8 y 14 caracteres.")
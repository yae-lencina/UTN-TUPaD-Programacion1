magnitud=int(input("Ingrese magnitud del terremoto: "))

if magnitud<3:
    print("Muy leve")
elif ((magnitud>=3) and (magnitud<4)):
    print("Leve.Ligeramente perceptible.\n")
elif((magnitud>=4) and (magnitud<5)):
    print("Moderado. Sentido por personas, pero generalmente no causa daños.\n")
elif((magnitud>=5) and (magnitud<6)):
    print("Fuerte. Puede causar daños en esctructuras debiles.\n")
elif((magnitud>=6) and (magnitud<7)):
    print("Muy fuerte. Puede causar daños significativos.\n")
elif(magnitud>=7):
    print("Extremo.Puede causar daños graves a gran escala.\n")
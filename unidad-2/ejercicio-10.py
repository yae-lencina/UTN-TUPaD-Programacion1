dia=int(input("Ingrese dia: "))
mes=int(input("Ingrese mes [1/12]: "))
hemisferio=input("Ene que hemisferio te encuentras?: ").upper()

if(hemisferio == "S"):
    if (((mes == 12) and (dia>=21)) or (mes>=1) and (mes<3)) or ((mes==3) and (dia<=20)):
        print("Verano")
    elif (((mes==3) and (dia>=21)) or ((mes>3) and (mes < 6)) or ((mes == 6) and (dia<=20))):
        print("otoño")
    elif (((mes==6) and (dia>=21)) or ((mes>6) and (mes < 9)) or ((mes == 9) and (dia<=20))):
        print("Ivierno")
    elif (((mes==9) and (dia>=21)) or ((mes>9) and (mes < 12)) or ((mes == 12) and (dia<=20))):
        print("Primavera")
elif (hemisferio == "N"):
    if (((mes == 12) and (dia>=21)) or (mes>=1) and (mes<3)) or ((mes==3) and (dia<=20)):
        print("Invierno")
    elif (((mes==3) and (dia>=21)) or ((mes>3) and (mes < 6)) or ((mes == 6) and (dia<=20))):
        print("Primavera")
    elif (((mes==6) and (dia>=21)) or ((mes>6) and (mes < 9)) or ((mes == 9) and (dia<=20))):
        print("Verano")
    elif (((mes==9) and (dia>=21)) or ((mes>9) and (mes < 12)) or ((mes == 12) and (dia<=20))):
        print("Otoño")
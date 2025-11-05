import math
def area_circulo (radio):
    area = math.pi * (radio**2)
    return area

def perimetro_circulo(radio):
    perimetro= 2*math.pi*radio
    return perimetro

r=float(input("Ingrese radio del circulo para calcular area y perimetro: "))
print("El area del circulo es: ", area_circulo(r))
print("El perimetro del circulo es: ",perimetro_circulo(r))
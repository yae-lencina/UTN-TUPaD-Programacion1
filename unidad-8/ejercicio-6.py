#6-Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número entero positivo: "))

print("La suma de los dígitos es:", suma_digitos(num))
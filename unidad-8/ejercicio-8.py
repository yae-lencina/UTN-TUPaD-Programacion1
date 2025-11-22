#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del númer


def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    
    
    ultimo = numero % 10
    
    
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

n = int(input("Ingrese un número entero positivo: "))
d = int(input("Ingrese el dígito a buscar (0-9): "))

print("El dígito aparece:", contar_digito(n, d), "veces.")
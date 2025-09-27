import random
lista_random=[]
lista_par=[]
lista_impar=[]
for i in range (15):
    numero=random.randint(1,100)
    lista_random.append(numero)
    if (numero%2==0):
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print("Mi lista random: ",lista_random)
print("Mi lista par ",lista_par, " cantidad de elementos: ", len(lista_par))
print("Mi lista impar ",lista_impar, " cantidad de elementos: ", len(lista_impar))
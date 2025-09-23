import random
num_aleatorios = [random.randint(1,100) for i in range (20)]
print(num_aleatorios)

from statistics import mode, median, mean
media=int(mean(num_aleatorios))
moda=float(mode(num_aleatorios))
mediana=float(median(num_aleatorios))

print("La media es: ", media, "\nLa moda es: ", moda, "\nLa mediana es: ", mediana )

if ((media>mediana) and (mediana>moda)):
    print("sesgo positivo.")
elif((media<mediana) and (mediana<moda)):
    print("Sesgo negativo.")
elif((media==mediana) and (media==moda)):
    print("Sin sesgo.")
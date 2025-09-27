lista=[]

for i in range (5):
 producto=input("Ingrese producto: ")
 lista.append(producto)

print("mi lista original: ",lista)
ordenado=sorted(lista)
print("Mi lista ordenada: ",ordenado)

elemento=input("Que elemento desea eliminar? : ")

if (elemento in ordenado):
 ordenado.remove(elemento)
 print(elemento,"Fue eliminado de la lista.")

print("Mi lista final: ",ordenado)

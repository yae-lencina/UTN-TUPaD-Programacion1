lista=[1,5,3,6,2,7,8]
derecha=[]
ultimo=lista[-1]
resto=lista[:-1]
derecha=[ultimo] + resto
#print(ultimo)
#print(resto)
print("mi lista original: ",lista)
print("mi lista corrida a la derecha: ",derecha)
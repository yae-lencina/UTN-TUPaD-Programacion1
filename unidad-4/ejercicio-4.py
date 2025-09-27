datos=[1,3,5,3,7,1,9,5,3]
nueva=[]

for i in datos:
 if i not in nueva:
  nueva.append(i)

print(nueva)
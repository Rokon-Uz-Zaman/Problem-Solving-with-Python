#find how many number smaller than the input

ar=[1,2,3,4]

input=3
ar2=[]

for element in ar:
   if element < input: 
      ar2.append(element)

print(len(ar2))      

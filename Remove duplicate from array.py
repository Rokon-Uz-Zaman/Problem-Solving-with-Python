"""Remove duplicate elements from array 

Example1 :
input: [1,2,2,3] output: [1,2,3]

Example2 :
input: [1,2,3,4,4,5] output: [1,2,3,4,5]   """


# using loop 

ar=[1,2,3,4,4,5]


for element in ar:
  if ar.count(element) >1:
     ar.remove(element)
     
print(ar)


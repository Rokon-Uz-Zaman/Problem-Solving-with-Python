blank=[]

target=int(input())

ar=[2,7,11]


for element in ar:
  find=target-element
  if find in ar:
    blank.append(find)
    
  
print(blank)

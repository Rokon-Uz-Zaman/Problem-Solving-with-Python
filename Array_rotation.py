#array rotation

a=[1,2,3,4,5]
rotation=1

for i in range(rotation):
   last_index=a.index(a[-1])
   last=a.pop(last_index)
   a.insert(0,last)
    
print(a)   

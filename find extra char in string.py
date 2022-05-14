#Finding extra char in string 

string1=input()
string2=input()

for element in string2:
    #conditon1 : abcd , abcde
    if element not in string1: 
       print(element) 
    
    #condtion 2 : abcd , abcdd
    elif element in string1 and string2.count(element)>1 :
      print(element)
      break  
       

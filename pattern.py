
'''
Print the pattern :

***********
**********
*********
********
*******
******
*****
****
***
**
*
'''


#controling row using loop 1

for i in range(11,0,-1):
    print("")
    
    #controlling every (squre) column using loop 2
    for j in range(i) :
        print("*",end='')

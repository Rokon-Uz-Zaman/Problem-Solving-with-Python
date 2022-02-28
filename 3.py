
'''
*
**
***
****
*****
******
*******
********
*********
**********
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

######## part 1: first half ########

#controling row using loop 1

for i in range(11):
    print("")
    #controlling every (squre) column using loop 2
    for j in range(i) :
        print("*",end='')




##### Part 2 : second half ( reverse of first half ) #####

#controling row using loop 1

for k in range(11,0,-1):
    print("")
    #controlling every (squre) column using loop 2
    for l in range(k) :
        print("*",end='')

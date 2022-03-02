#How to reverse every word of a sentense ( string)

rev=''

sentense="Banglasesh is nice country"

sentense=sentense.split()
sentense.reverse()



for element in sentense:
    rev=rev+" "+element
print(rev)    



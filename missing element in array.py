"""Given an array nuns 
containing n distinct numbers in the range [e, n], 
return the only number in the range that is missing from the array """

arr=[0,1,3]
arr2=list(range(len(arr)+1))

for element in arr2:
  if element not in arr:
    print(element)

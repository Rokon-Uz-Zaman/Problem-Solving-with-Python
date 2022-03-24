"""Remove duplicate elements from sorted array 
with returning how many duplicates

Example1 :
input: [1,2,2,3] output: [1,2,3] Number of duplicates is 1

Example2 :
input: [1,2,3,3,4,4,5] output: [1,2,3,4,5]  Number of duplicates is 2 """


ar=[1,2,3,3,4,4,5]

print(set(ar))

print(f"Number of duplicates is {len(ar)-len(set(ar))}")

'''
Given an array of integers, calculate the ratios of its elements
that are positive, negative, and zero.Print the decimal value of 
each fraction on a new line with places after the decimal.
'''


n=int(input())
arr=map(int,input().split())
#arr=[1,1,0,-1,-1]

pos =0
neg=0
zero=0

for i in arr:
  if i > 0:
    pos= pos+1
  if i <0:
    neg= neg + 1
  if i == 0:
    zero=zero+1

pos=pos/5
neg=neg/5
zero=zero/5

print(f'{pos:.6f}')
print(f'{neg:.6f}')
print(f'{zero:.6f}')

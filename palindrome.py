""""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
"""


num=input()
rev=num[::-1]

def palindrome_checker():
  if num == rev :
     return True

palindrome_checker()
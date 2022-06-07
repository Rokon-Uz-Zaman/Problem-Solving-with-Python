'''
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.
Input The input file contains an integer N.
Output Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
Input Sample 556
Output Sample  0:9:16
'''



given=140153

h=int(given/3600)
given=given- h*3600


m=int(given/60)
given=given - m*60

s=given

print(f"{h}:{m}:{s}")

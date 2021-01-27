'''
Write a Python program to print 
all even integers from 20 down to 0, and 0 up to 20.  
'''

i = 20 #iterator

#Each execution of the loop is called an iteration.

while i >= 0:
    if i % 2 == 0:
        print(i,20-i)
    i-= 1


'''
Write a program to receive an integer n from the user
and print all even integers from n to 0. 
'''

n = eval(input())
i = n
if n % 2 != 0:
    i-=1
    
while i > 1:
    print(i)
    i-=2



'''
Write a Python program to receive a LIST of numbers from the user.
Print the sum of every two consecutive numbers starting from the
first number until the last number.

'''

L = input().split()
L = list(map(eval,L))

i = 0
n = len(L)

while (i+1) < n:
    print(L[i]+L[i+1], end=' ')
    i+=1
    



'''
Write a program to receive numbers from the user.
When the user finishes entering the numbers, print
the sum of the numbers. Assume the user is finished when
the value is -1. 
'''

s = 0 
while True:
    value = int(input('Enter a value: '))
    if value == -1:
        break
    s += value

print('The sum is',s)

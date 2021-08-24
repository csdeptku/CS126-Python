'''
Check if a string has either an integer or a float in it. 
This program does not take care of negative values or spaces.
'''

s = input()

if s.isdigit():
    print(s,'is an integer.')
else:
    L = s.split('.')
    if len(L) == 2 and L[0].isdigit() and L[1].isdigit():
        print(s,'is a real number.')
    else:
        print(s,'is not numeric.')



'''
Write a program to receive numbers from the user.
When the user finishes entering the numbers, print
the sum of the numbers. Assume the user is finished when
the value is END. 
'''

s = 0 
while True:
   value = input()
   if value == 'END':
      break
   s+= eval(value)

print(s)

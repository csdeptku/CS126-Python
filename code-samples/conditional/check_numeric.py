'''
Check if a string has either an integer or a float in it. 
'''
s = input('Enter a value: ') 
if s.replace('.','').strip().isnumeric() and s.count('.') < 2: 
   print(s,'is numeric')
else:
   print(s, 'is not numeric') 

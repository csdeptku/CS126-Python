'''
Check if a string has either an integer or a float in it. 
'''
s = input('Enter a value: ') 
if s.replace('.','').rstrip().lstrip().isnumeric() and s.count('.') < 2: 
   print(s,'is numeric')
else:
   print(s, 'is not numeric') 

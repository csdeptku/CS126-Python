'''
This program prints a multiplication table.
'''

for i in range(1,10):
   for j in range(1,10):
      print(str(i)+'x'+str(j),i*j, end=' ')
   print()

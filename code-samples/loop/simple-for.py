
L = list(map(eval,input().split()))

'''
This loop will not change the values of L
'''
for x in L:
   x = x**2

print(L) 

'''
This loop will change the values of L
'''
for i in range(len(L)):
   L[i] = L[i]**2

print(L)


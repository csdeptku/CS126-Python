def square(x):
   return x**2

def maximum(x,y,z):
   if x>=y and x>z:
      return x
   if y > z:
      return y
   return z

def absolute(x):
   if x>=0:
      return x
   return -x


def summation(L):
   s=0
   for x in L:
      s+=x
   return s

def length(L):
   i=0
   for x in L:
      i+=1
   return i

def maxall(L):
   m = L[0]
   for x in L:
      if m < x:
         m = x
   return m 

def index(L,e):
   i = 0 
   for x in L:
      if x == e: 
         return i
      i+=1
   return i+1 

L=input().split()
L=list(map(eval,L))

s = summation(L)
n = length(L)
m = maxall(L)
print('Sum:',s)
print('Length:',n)
print('Maximum:',m)
if n>=3:
   print('Max of first three numbers:', maximum(L[0],L[1],L[2]))

print('Squared:')
print(list(map(square,L)))
print('Index of',1,'is',index(L,1))


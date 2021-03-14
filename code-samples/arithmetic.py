'''
Perform a long division, assuming N,D > -1 and N,D are both integer.  
'''
def longdiv(N,D):
   q,r=0,0
   if D==0: 
      raise ValueError('Division by zero!')
   if N < D:
      return 0,N
   if N == D: 
      return D,0 
   i = 1
   while i*D <= N: 
      i+=1
   q=i-1
   r=N-q*D 
   return q,r

def power(n,k):
   p = 1
   negative = False
   if k < 0: 
       negative = True
       k = -k 
   while k >= 1:
       p*=n
       k-=1
   if negative:
       p = 1/p
   return p 


'''
Testing code
'''

n = int(input('n: '))
k = int(input('k: '))

print(power(n,k))

N = int(input('N: '))
D = int(input('D: '))

print(longdiv(N,D))
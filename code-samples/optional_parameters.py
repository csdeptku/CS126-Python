from math import sqrt, inf 

def f(x,y,a=inf,b=inf):
   s,t = 0,0
   if a < inf: 
      s = x+y*a 
   if b < inf: 
      t = x+y*2*sqrt(b)
   return s,t,x+y


print(f(2,5))
print(f(2,5,b=4))
print(f(2,5,a=2,b=4))

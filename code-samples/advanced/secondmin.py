from math import inf
def secondmin(L):
   m1,m2=inf,inf
   for x in L:
      if x <= m1:
         m2 = m1 
         m1  = x
      elif x < m2: 
         m2 = x 
   return m2

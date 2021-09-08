from math import inf
def secondmin(L):
   m1,m2=inf,inf
   for x in L:
      tmp = None
      if x <= m1:
         tmp = m1 
         m1  = x
      if (tmp is not None) and tmp<m2:
         m2 = tmp 
   return m2

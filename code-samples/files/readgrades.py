'''
Read grades of the midterm and the final for students
from a file called students.csv and print the mean and
the standard deviation of the grades. Round both results
to three decimal palces.
'''
def loaddata():
   f=open('students.csv','r')
   data = [eval(x) for x in f] 
   return data 

def mean(D):
   s = 0 
   i = 0 
   for x in D:
      s+=x
      i+=1 
   return round(s/i,3)

def stddev(D,mu):
   std = 0
   n = 0 
   for x in D: 
      std += (x-mu)**2
      n+=1 
   std /= n 
   return round(std**.5,3)

data = loaddata()
midterm = []
final = [] 
for x in data: 
   midterm.append(x[0])
   final.append(x[1])
mu = mean(midterm)
sd = stddev(midterm,mu)
print('Mean (midterm):', mu,'Standard deviation (midterm):',sd)
mu = mean(final)
sd = stddev(final,mu)
print('Mean (final):', mu,'Standard deviation (final):',sd)


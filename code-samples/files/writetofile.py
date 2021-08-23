'''
In this program, we will read student grades from a file
that contains the midterm grade followed by the final grade. 
Next, we will give each student a 5% increase for the midterm
and a 8% increase for the final. We will write the new grades
on a new file. 
'''

def loaddata():
   f=open('students.csv','r')
   midterm=[]
   final=[]
   for line in f:
      line = eval(line)
      midterm.append(line[0])
      final.append(line[1])
   return midterm,final

def dumpdata(midterm,final):
   f=open('students_inc.csv','w')
   n = len(midterm)
   for i in range(n):
      row = midterm[i],final[i]
      print(row,file=f)
   f.close()

midterm,final = loaddata()
midterm = [round(mid*1.05,2) for mid in midterm]
final   = [round(fin*1.08,2) for fin in final]

dumpdata(midterm,final)

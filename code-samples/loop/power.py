'''
Use a loop to compute n to the power k. 
'''
n=int(input())
k=int(input())

p = 1

for i in range(abs(k)):
    p*=n

if k < 0:
    p=1/p

print(p)

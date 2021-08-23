x = 10

def f(x):
   x = 2

def g():
   print(x)

def h():
   global x
   x = 2

g()
f(x)
print(x)
h()
print(x)

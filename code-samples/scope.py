'''
Trace this program without running it and
see if you can produce the correct output
by checking your output against Python's. 
'''
x = 1
y = 2

def f(x):
    x = 3
    return x
def g(x):
    x = 4
    def f(x):
        x = 5
        return x
    return x
def h():
    global x
    global z
    z = 4
    x = 6
    return x
def h2(y=None):
    if y is None:
        x = 6
    else:
        x = 16
    return x

print(x,y,f(x),g(x),h(),x,z)


'''
Problem: find a root of a real-valued functions, defined as the point
x that satisfy f(x) = 0. 
Solution: use Netwon's method, which approximates the root x using the first
derivative of the function f: 
x_1 = x_0 - f(x_0)/f'(x_0). 
Given some conditions, x_1 is closer to the root x than x_0. 
'''

'''
Finding the square root of a as x. 
'''
def square_root(x,a): 
	return x**2-a

'''
First derivative of square_root. 
'''
def square_root_fd(x):
	return 2*x 


'''
x_0 is the initial guess for the root x. 
f is the function and g is its first derivative. 
'''
def newton_sqrt(x_0,a): 
	max_it = 1000
	epsilon = 0.0001
	m = 1 
	x = 0 
	x_0 = a*0.01
	for i in range(max_it):
		f = square_root(x_0,a)
		g = square_root_fd(x_0)   
		x = x_0 - m*(f/g)
		if abs(x-x_0) < epsilon: 
			break 
		x_0 = x  
	x = round(x,4)
	return x,i 


'''
Test case: find square root of an integer input by the user.
'''
a = int(input('Enter an integer: '))
ans,i = newton_sqrt(1,a)
print('The square root is:',ans,'found in',i,'iterations.')
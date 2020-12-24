#This program computes the body mass index of a person, given the person's height and weight. 

m = input('Enter your mass in kilograms: ')
h = input('Enter your height in meters: ') 

m = float(m)
h = float(h)

print(m/h**2)

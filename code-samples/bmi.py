#This program computes the body mass index of a person, given the person's height and weight. 

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight/((height*.01)**2)
bmi = round(bmi, 2)
print("BMI: ", bmi)

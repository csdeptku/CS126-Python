
#compute a person's body mass index

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight/((height*.01)**2)
bmi = round(bmi, 2)
print("BMI: ", bmi)

if bmi <= 18.5: 
   print("Underweight")
elif bmi <25:
   print("Normal weight")
elif bmi < 30:
   print("Overweight")
else: 
   print("Obesity")


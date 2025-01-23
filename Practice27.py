# CS 1101 - Week 09 - Exercise 09
print()
weight = float(input("Enter your weight in Kg : "))
height = float(input("Enter your height in m  : "))
bmi = ((weight) / (height**2))
print(f"BMI Value : {bmi}")
if bmi < 18.5:
    print("Category : Underweight")
elif bmi < 25:
    print("Category : Normal")
elif bmi < 30:
    print("Category : Overweight")
else:
    print("Category : Obese")

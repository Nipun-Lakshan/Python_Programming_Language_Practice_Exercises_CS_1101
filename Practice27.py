# CS 1101 - Week 09 - Exercise 09
print()
weight = float(input("Enter your weight in Kg : "))
height = float(input("Enter your height in m  : "))
bmi = ((weight) / (height**2))
print(f"BMI Value \t\t: {round(bmi, 2)}")
if bmi < 18.5:
    print("Category \t\t: Underweight")
elif bmi < 25:
    print("Category \t\t: Normal")
elif bmi < 30:
    print("Category \t\t: Overweight")
else:
    print("Category \t\t: Obese")

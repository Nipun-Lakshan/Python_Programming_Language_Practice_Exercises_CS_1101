# CS 1101 - Week 09 - Exercise 10
print()
current_reading = int(input("Enter Your Current Reading         : "))
previous_reading = int(input("Enter Your Previous Reading        : "))
units = current_reading - previous_reading
print(f"Number of Units Consumed Per Month : {units}")
if units <= 60:
    category = 1  # Lower Category
else:
    category = 0  # Upper Category

if category == 1:
    if units <= 30:
        
        total_cost = (units * 6) + 100
    else:
        total_cost = (30 * 6) + ((units - 30) * 9) + 250
else:
    if units <= 90:
        total_cost = (60 * 15) + ((units - 60) * 18) + 400
    elif units <= 120:
        total_cost = (60 * 15) + (30 * 18) + ((units - 90) * 30) + 1000
    elif units <= 180:
        total_cost = (60 * 15) + (30 * 18) + (30 * 30) + (
            (units - 120) * 42) + 1500
    else:
        total_cost = (60 * 15) + (30 * 18) + (30 * 30) + (60 * 42) + (
            (units - 180) * 65) + 2000
print(f"Total Bill                         : Rs. {total_cost}.00")
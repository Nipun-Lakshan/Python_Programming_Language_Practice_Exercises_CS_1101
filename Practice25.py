# CS 1101 - Week 09 - Exercise 07

# Code 01
print()
height = int(input("Enter the Height : "))
print()
for i in range(0, height):
    print("*" * (i + 1))

# Code 02
print()
height = int(input("Enter the Height : "))
print()
for i in range(0, height):
    for j in range(0, (i + 1)):
        print("*", end="")
    print()

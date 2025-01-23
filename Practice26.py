# CS 1101 - Week 09 - Exercise 08
print()
height = int(input("Enter the Height : "))
print()
for i in range(0, height):
    for j in range(0, (height - 1)):
        print(" ", end="")
    print("*" * (2 * (i + 1) - 1))
    height = height - 1

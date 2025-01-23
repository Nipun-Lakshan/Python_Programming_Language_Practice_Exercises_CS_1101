# CS 1101 - Week 10 - Practice 02

# For Loop - Basic Syntax - Code 01
print()
for x in range(1, 11):
    print(x)
print()

# For Loop - Basic Syntax - Code 02
for counter in range(1, 11):
    print(counter)
print()
print("Happy New Year")
print()

# For Loop - Basic Syntax - Code 03
for x in reversed(range(1, 11)):
    print(x)
print()

# For Loop - Basic Syntax - Code 04
print()
for x in range(1, 11, 2):
    print(x)

# For Loop - Basic Syntax - Code 05
print()
for x in range(1, 11, 3):
    print(x)

# For Loop - Basic Syntax - Code 06
print()
credit_card = "1234-5678-9012-5678"
for x in credit_card:
    print(x)

# For Loop - Basic Syntax - Code 07
print()
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# For Loop - Basic Syntax - Code 07
print()
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

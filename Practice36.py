# CS 1101 - Week 10 - Exercise 02 - Methods & Functions Which Related To Lists

# Importing Library From Python Standard Libraries
import random

# Header String Printing
print("\n====================")
print("Number Guessing Game")
print("====================\n")

# Logic Of The Game
while (True):
    feed = input("Shall We Start? (Y / N) : ")
    random_number = random.randint(0, 100)
    if feed in ('Y', 'y'):
        while (True):
            user_input = int(input("Guess any Number between 0 to 100 : "))
            if (user_input < 0 or user_input > 100):
                print("Invalid Input! Please enter a number between 0 to 100!")
                print("Try again!\n")
                continue
            else:
                if user_input < random_number:
                    print("Too Low!\n")
                elif user_input > random_number:
                    print("Too High!\n")
                else:
                    print("Well Done!\n")
                    break
    elif feed in ('n', 'N'):
        print("Thank you for coming!")
        break
    else:
        print("Invalid choice! Please enter 'Y' to start or 'N' to exit.\n")

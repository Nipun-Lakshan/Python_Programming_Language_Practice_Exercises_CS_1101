# CS 1101 - Week 10 - Exercise 04 - Dice Rolling Game

# Importing Library From Python Standard Libraries
import random

# Header String Printing
print("\n=================")
print("Dice Rolling Game")
print("=================\n")

# Logic Of The Game
while True:
    user_input = input("Roll the Dice? (Y/N) : ")
    if user_input in ('Y', 'y'):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(f"({dice_1}, {dice_2})")
        break
    elif user_input in ('N', 'n'):
        print("Thanks for Playing!")
        break
    else:
        print("Invalid Choice!\n")

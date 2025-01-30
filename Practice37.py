# CS 1101 - Week 10 - Exercise 03 - Number Guessing Game - Answer

# Importing Library From Python Standard Libraries
import random

# Header String Printing
print("\n====================")
print("Number Guessing Game")
print("====================\n")

# Logic Of The Game
while True:
    feed = input("Shall We Start? (Y / N) : ").strip().lower()

    if feed == 'y':
        random_number = random.randint(0, 100)
        print("\nA new number has been generated. Try to guess it!\n")

        while True:
            try:
                user_input = int(input("Guess any number between 0 to 100: "))

                if user_input < 0 or user_input > 100:
                    print(
                        "Invalid Input! Please enter a number between 0 to 100!\n"
                    )
                    continue

                if user_input < random_number:
                    print("Too Low!\n")
                elif user_input > random_number:
                    print("Too High!\n")
                else:
                    print("Well Done! You guessed it correctly!\n")
                    break

            except ValueError:
                print("Invalid input! Please enter a valid number.\n")
                continue

    elif feed == 'n':
        print("Thank you for coming! Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 'Y' to start or 'N' to exit.\n")

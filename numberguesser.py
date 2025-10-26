# A program where the computer picks a random number (1-10), and the user guesses until correct, using a loop to continue until the guess matches.

import random

number_to_guess = random.randint(1, 10)
user_guess = None
while user_guess != number_to_guess:
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Very nice! Umepata answer.")
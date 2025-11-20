# A program that simulates rolling a dice with a user-specified number of sides and rolls, using the random module.

# Importing the Random Module
import random

# Dice Roller Function
def roll_dice(sides, rolls):
    results = [random.randint(1, sides) for _ in range(rolls)]
    return results

# User Input
sides = int(input("Enter number of sides on the dice: "))
rolls = int(input("Enter number of rolls: "))

# Calling the function (rolling the dice) then displaying results.
dice_results = roll_dice(sides, rolls)
print("Dice rolls:", dice_results)

print("Sum of rolls:", sum(dice_results))
print("Average of rolls:", sum(dice_results) / len(dice_results))



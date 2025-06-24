import random

def roll_dice(num_dice, num_sides):
    return [random.randint(1, num_sides) for _ in range(num_dice)]

#print(roll_dice(2,6))

def calculate_sum(dice_rolls):
    return sum(dice_rolls)

def calculate_average(dice_rolls):
    if not dice_rolls:
        return 0
    return sum(dice_rolls) / len(dice_rolls)

def roll_query():

    global description
    description = "Make a search query using your default web browser."

    number_of_dice = int(input("Enter the number of dice to roll: "))
    number_of_sides = int(input("Enter the number of sides on each die: "))
    rolls = roll_dice(number_of_dice, number_of_sides)
    print(f"Rolled: {rolls}")
    print(f"Sum: {calculate_sum(rolls)}")
    print(f"Average: {calculate_average(rolls):.2f}")
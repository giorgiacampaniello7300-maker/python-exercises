import random

number_of_dice = int(input("Enter a number of dice to roll: "))
total_rolls = 0

for number in range(number_of_dice):
    die_roll = random.randint(1, 6)
    total_rolls = total_rolls + die_roll

print(f"The sum of the numbers is: {total_rolls}")
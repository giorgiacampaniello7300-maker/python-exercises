import random

maximum_number = int(input("Enter the maximum number on the dice: "))

def dice_roll(sides_number):
    result = random.randint(1, sides_number)
    return result

result = dice_roll(maximum_number)

while result != maximum_number:
    print(result)
    result = dice_roll(maximum_number)

print(result)
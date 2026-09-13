import random

def dice_roll():
    result = random.randint(1, 6)
    return result

result = dice_roll()

while result != 6:
    print(result)
    result = dice_roll()

print(result)
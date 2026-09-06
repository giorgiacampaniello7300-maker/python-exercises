import random

random_integer = random.randint(1, 10)

guess = int(input("Guess the number: "))

while guess != random_integer:
    if guess > random_integer:
        print("Too high")
    elif guess < random_integer:
        print("Too low")
    guess = int(input("Guess the number: "))

print("Correct")
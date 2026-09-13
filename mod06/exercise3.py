integer = int(input("Enter an integer: "))

for divisor in range(2, integer):
    if integer % divisor == 0:
        print("This number is not a prime number.")
        break

else:
    print("This number is a prime number.")
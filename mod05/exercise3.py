numbers = input("Enter a number: ")
numbers_in_total = 0

while numbers != "":
    numbers = float(numbers)

    if numbers_in_total == 0:
        smallest_number = numbers
        largest_number = numbers

    if numbers < smallest_number:
        smallest_number = numbers

    if numbers > largest_number:
        largest_number = numbers

    numbers_in_total = numbers_in_total + 1
    numbers = input("Enter a number: ")

print(f"{smallest_number} {largest_number}")
  
   
def integers(numbers):
    total = 0 
    for n in numbers: 
        total = total + n
    return total 

numbers = [1, 2, 3, 4, 5]
integers(numbers)

print(integers(numbers))
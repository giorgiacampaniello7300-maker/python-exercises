def integers(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers

numbers = [1, 2, 3, 4, 5]

even_numbers = integers(numbers)

print(numbers)
print(even_numbers)
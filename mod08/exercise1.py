number = int(input("Enter a number of a month: "))

seasons = ("spring", "summer", "autumn", "winter")

if number == 3 or number == 4 or number == 5:
    season = seasons[0]
elif number == 6 or number == 7 or number == 8:
    season = seasons[1]
elif number == 9 or number == 10 or number == 11:
    season = seasons[2]
elif number == 12 or number == 1 or number == 2:
    season = seasons[3]

print(f"The corrisponding season is {season}.")
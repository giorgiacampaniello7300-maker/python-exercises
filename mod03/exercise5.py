talents = float(input("Enter a mass in talents: "))
pounds = float(input("Enter a mass in pounds: "))
lots = float(input("Enter a mass in lots: "))

lots_in_grams = (1 * 13.3) * lots
pounds_in_grams = (32 * 13.3) * pounds
talents_in_grams = (20 * 32 * 13.3) * talents
total_in_grams = lots_in_grams + pounds_in_grams + talents_in_grams
full_kilograms = int(total_in_grams // 1000)
grams_left = total_in_grams % 1000

print (f"The weight in modern units:\n{full_kilograms} kilograms and {grams_left:.2f} grams.")
import math

def pizza(diameter_cm, price_euros):
    radius_cm = diameter_cm / 2
    radius_m = radius_cm / 100
    area = math.pi * radius_m ** 2
    unit_price = price_euros / area
    return unit_price

diameter_1 = float(input("Enter the diameter of the first pizza: "))
price_1 = float(input("Enter the price of the first pizza: "))
diameter_2 =  float(input("Enter the diameter of the second pizza: "))
price_2 = float(input("Enter the price of the second pizza: "))

unit_price_1 = pizza(diameter_1, price_1)
unit_price_2 = pizza(diameter_2, price_2)

if unit_price_1 < unit_price_2:
    print("Pizza 1 provides better value for money.")
elif unit_price_1 == unit_price_2:
    print("Both pizzas provide the same value for money.")
else: 
    print("Pizza 2 provides better value for money.")
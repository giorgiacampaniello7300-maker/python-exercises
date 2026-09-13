def gasoline_gallons(gallons):
    result = gallons * 3.785
    return result

volume_in_gallons = float(input("Enter a volume in gallons: "))

while volume_in_gallons >= 0: 
    result = gasoline_gallons(volume_in_gallons)
    print(f"Volume in gallons converted to liters: {result}.")
    volume_in_gallons = float(input("Enter a volume in gallons: "))
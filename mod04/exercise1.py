centimeters = float(input("Enter the length of a zander in centimeters: "))

if centimeters < 42:
    difference_in_centimeters = 42 - centimeters
    print("Release the fish back into the lake.")
    print(f"The cought fish was {difference_in_centimeters} centimeters below the size limit.")
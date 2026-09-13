inventory  = ["water", "coffee", "apple", "sandwich"]

def collect_item():
    item = input("What item did you collect? ")
    inventory.append(item)
    return

def items_list():
    print("Here is what you have: ")
    for item in inventory:
        print(item)
    return

def item_use():
    purpose = input("Would you like to use the item or exchange it? ")

    if purpose == "Use":
        print("Item used.")

    elif purpose == "Exchange":
        old_item = input("Which item would you like to exchange? ")
        inventory.remove(old_item)
        print("Item exchanged.")
        new_item = input("Which new item did you receive? ")
        inventory.append(new_item)
    return

def energy():
    print("You can continue to explore now!")
    return

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 12:
    print("You are a minor, too young to explore Italy alone. The game will shut down.")
else:
    print("Hello, "+name+"! \nMain Menu: \nExplore \nEat \nCollect \nUse \nInventory \nMap")

    command = input("Enter command: ")

    while command != "lopeta":

        if command == "Explore":
            print("You are walking around.")

        elif command == "Eat":
            print("Energy restored.")
            energy()

        elif command == "Collect":
            print("Wow! Great job!")
            collect_item()

        elif command == "Use":
            print("Good choice!")
            item_use()

        elif command == "Inventory":
            print("Welcome to the Inventory.")
            items_list()

        elif command == "Map":
            print("You opened the map.")

        else:
            print("Invalid command.")
    
        print("\nMain Menu: \nExplore \nEat \nCollect \nUse \nInventory \nMap")
        command = input ("Enter command: ")

    print ("Execution stopped.")
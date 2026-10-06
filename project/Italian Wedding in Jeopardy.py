from game_parts import Player, Location, Item 
import json

water = Item("Water", 5)
coffee = Item("Coffee", 3)
apple = Item("Apple", 3)
sandwich = Item("Sandwich", 3)
cooler_bag = Item("Cooler bag", 1)
grana_padano = Item("Grana Padano", 2)

inventory  = [water, coffee, apple, sandwich]
milan_items = [cooler_bag, grana_padano]

milan = Location("Milan", milan_items)
florence = Location("Florence", [])

def collect_item():
    item = input("\nWhat item did you collect? ")
    for m in milan_items: 
        if item == m.name: 
            milan_items.remove(m)
            inventory.append(m)
            print(f"\n{m.name} has been added to the inventory.")
            if m == cooler_bag:
                print("\nKeep exploring. You still need to find ingredients for the wedding.")
            elif m == grana_padano:
                print("\nYou are ready to leave Milan. Choose 'Explore' to move to Florence.")
            break
    return

def items_list():
    print("Here is what you have: ")
    for item in inventory:
        print(item.name)
    return

def item_use():
    purpose = input("Would you like to use the item or exchange it? ")

    if purpose == "Use":
        print("Item used.")
    elif purpose == "Exchange":
        print("Exchanging items is not available yet.")
    else:
        print("Invalid choice.")
    return

def energy():
    print("You can continue to explore now!")
    return

def save(player, age, answer,): 
    item_names = []
    for item in player.items:
        item_names.append(item.name)
    save_data = {"name": player.name, "age": age, "answer": answer, "location": player.location.name, "items": item_names}

    with open("project/save.json", "w") as file:
        json.dump(save_data, file)
    print("Game saved.")

def load():
    with open("project/save.json", "r") as file:
       save_data = json.load(file)
       return save_data
    
with open("project/intro.txt", "r") as file:
    data = file.read()
    print(data)

with open("project/instructions.txt", "r") as file:
    data = file.read()
    print(data)

game_answer = input("New game or continue game? Enter: New / Continue: ")

while game_answer != "New" and game_answer != "Continue":
    game_answer = input("Enter 'New' or 'Continue': ")

if game_answer == "Continue":
    try: 
        saved_game = load()
    except FileNotFoundError:
        print("No saved game found. Starting a new game.")
        game_answer = "New"

if game_answer == "New":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    answer = ""
    location = milan

elif game_answer == "Continue":
    name = saved_game["name"]
    age = saved_game["age"]
    answer = saved_game["answer"]

    all_items = [water, coffee, apple, sandwich, cooler_bag, grana_padano]
    inventory = []

    for item in all_items:
        if item.name in saved_game["items"]:
            inventory.append(item)

    for item in inventory:
        if item in milan_items:
            milan_items.remove(item)

    if saved_game["location"] == "Milan":
        location = milan
    elif saved_game["location"] == "Florence":
        location = florence

    print("Saved game loaded.")

if age < 12:
    print("You are a minor, too young to explore Italy alone. The game will shut down.")
else:
    print("\nMain Menu: \nExplore \nEat \nCollect \nUse \nInventory \nSave\n")

    player = Player(name, inventory, location)
    print("Hello chef! You are now in " + player.location.name + " and you need to find some ingredients for the wedding menu. Explore this beautiful city.\n")

    command = input("Enter command: ")

    while command != "lopeta":

        if command == "Explore":
            if player.location == milan:
                if cooler_bag not in inventory: 
                    print("\nOh, an outside market! That Cooler bag seems nice. Collect it, it's free!")

                elif cooler_bag in inventory and grana_padano not in inventory and answer != "No thank you":
                    print("\nOld woman: Hello! Are you a tourist visiting Milan?")
                    print("\nChef: Oh no, I'm actually a chef. I'm looking for ingredients because I'll be cooking for a wedding in Sicily.")
                    print("\nOld woman: Wow, that's amazing! Would you like to take this Grana Padano? It's typical from here.")
                    print("\nChoose 'Collect' and type 'Grana Padano'.")
                    print("If you don't want it, type 'No thank you' and press 'Enter'.")

                    answer = input("Your reply (Collect / No thank you): ")

                    if answer == "Collect":
                        collect_item()
                    elif answer == "No thank you":
                        print("\nOld woman: No problem, enjoy your trip.")
                        print("\nYou are ready to leave Milan. Choose 'Explore' to move to Florence.")
                    else:
                        print("Invalid reply.")

                elif cooler_bag in inventory and (grana_padano in inventory or answer == "No thank you"):
                    player.moving(florence)
                    print(f"\nYou are now in {player.location.name}.")

        elif command == "Eat":
            print("\nEnergy restored.")
            energy()

        elif command == "Collect":
            print("\nWow! Great job!")
            collect_item()

        elif command == "Use":
            print("\nGood choice!")
            item_use()

        elif command == "Inventory":
            print("\nWelcome to the Inventory.")
            items_list()

        elif command == "Save":
            save(player, age, answer)

        else:
            print("\nInvalid command.")
    
        print("\nMain Menu: \nExplore \nEat \nCollect \nUse \nInventory \nSave\n")
        command = input ("Enter command: ")

    print ("Execution stopped.")
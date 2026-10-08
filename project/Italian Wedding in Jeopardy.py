from game_parts import Player, Location, Item 
import json

# Create the ingredients and supplies used in the game
water = Item("Water", 5)
coffee = Item("Coffee", 3)
apple = Item("Apple", 3)
sandwich = Item("Sandwich", 3)
cooler_bag = Item("Cooler bag", 1)
grana_padano = Item("Grana Padano", 2)
steaks = Item("Steaks", 30)
potatoes = Item("Potatoes", 60)
pasta = Item("Pasta", 6)
eggs = Item("Eggs", 60)
guanciale = Item("Guanciale", 6)
flour = Item("Flour", 3)
pecorino = Item("Pecorino", 3)
rice = Item("Rice", 3)
mushrooms = Item("Mushrooms", 6)
cake = Item("Cake", 1)
cupcakes = Item("Cupcakes", 30)

# Create the inventory and the items available in each city 
inventory  = [water, coffee, apple, sandwich]
milan_items = [cooler_bag, grana_padano]
florence_items = [steaks, potatoes]
rome_items = [pasta, eggs, guanciale, flour, pecorino]
naples_items = [rice, mushrooms]
taormina_items = [cake, cupcakes]

# Create the locations with their list of available items
milan = Location("Milan", milan_items)
florence = Location("Florence", florence_items)
rome = Location("Rome", rome_items)
naples = Location("Naples", naples_items)
taormina = Location("Taormina", taormina_items)

all_items = [water, coffee, apple, sandwich, cooler_bag, grana_padano, steaks, potatoes, pasta, eggs, guanciale, flour, pecorino, rice, mushrooms, cake, cupcakes]
all_locations = [milan, florence, rome, naples, taormina]

# The cheese task starts as incomplete
cheese_ready = False

# Move an item from its location to the player's inventory
def collect_item(item, location):
    location.items.remove(item)
    inventory.append(item)
    print(f"\n{item.name} has been added to the inventory.")
    if item == cooler_bag:
        print("\nYour cooler bag will help you carry ingredients that need to stay cool.")
    elif item == grana_padano:
        print("\nYou are ready to leave Milan. Choose 'Travel' to move to Florence.")
    return

# Show the inventory items and their quantities
def items_list():
    print("Here is what you have: ")
    for item in inventory:
        print(f"{item.name}: {item.quantity}")
    return

# Let the chef keep, exchange or buy cheese in Rome
def item_use(player):
    if player.location != rome or guanciale not in inventory:
        print("\nThere is nothing to use or exchange yet.")
        return False
    if pecorino in inventory:
        print("\nYour Pecorino is ready for the wedding.")
        return True
    if grana_padano in inventory:
        cheese_choice = input("\nWould you like to use the Grana Padano for the carbonara or exchange it with the Pecorino? Use / Exchange: ")
        if cheese_choice == "Use":
            print("\nYou keep the Grana Padano for the wedding.")
            return True
        elif cheese_choice == "Exchange":
            inventory.remove(grana_padano)
            collect_item(pecorino, player.location)
            print("\nYou exchanged your Grana Padano for the Pecorino.")
            return True
        else:
            print("\nInvalid choice.")
            return False
    else:
        print("\nYou have no cheese. You buy Pecorino in Rome.")
        collect_item(pecorino, player.location)
        return True

# Move to the next city only when the current tasks are completed
def travel(player, answer, cheese_ready):
    if player.location == milan:
        if cooler_bag not in inventory or (grana_padano not in inventory and answer != "No thank you"):
            print("\nFinish exploring Milan before travelling.")
            return

        transport = input("\nHow will you travel to Florence? Train / Bus / Car: ") 

        if transport == "Train":
            print("\nOn the train you meet tourists and talk about Italian food.")
            player.moving(florence)
        elif transport == "Bus":
            print("\nOh no! The bus is delayed. After waiting for a bit, you finally depart to Florence.")
            player.moving(florence)
        elif transport == "Car":
            print("You meet travellers driving to Florence. They offer you a ride.")
            reply = input("Would you like to join them? Yes / No: ")
            if reply == "Yes":
                print("You travel to Florence together.")
                player.moving(florence)
            elif reply == "No":
                print("\nYou are still in Milan. Choose 'Travel' to arrange another journey.")
            else:
                print("Invalid reply.")
        else: 
            print("\n Invalid transport. Choose 'Travel' to try again.")

    elif player.location == florence:
        if steaks in inventory and potatoes in inventory:
            print("\nYou board a train to Rome.")
            player.moving(rome)
        else:
            print("\nCollect steaks and potatoes before travelling.")

    elif player.location == rome:
        if steaks.quantity == 30 and pasta in inventory and eggs in inventory and guanciale in inventory and cheese_ready:
            print("\nYou board a train to Naples.")
            player.moving(naples)
        else:
            print("\nFinish collecting the ingredients and choosing your cheese.")

    elif player.location == naples:
        if rice in inventory and mushrooms in inventory:
            print("\nYou travel by bus and ferry to Sicily, then continue to Taormina.")
            player.moving(taormina)
        else:
            print("\nCollect rice and mushrooms before travelling.")

    else:
        print("\nThere is no journey available from here yet.")
        return
    
    print(f"\nYou are now in {player.location.name}.")

# Save the player's progress and details
def save(player, age, answer, cheese_ready): 
    saved_items = {}
    for item in player.items:
        saved_items[item.name] = item.quantity

    save_data = {
        "name": player.name,
        "age": age,
        "answer": answer,
        "location": player.location.name,
        "items": saved_items,
        "cheese_ready": cheese_ready
        }

    with open("project/save.json", "w") as file: # Write the game progress on the file, replacing the previous one
        json.dump(save_data, file)
    print("Game saved.")

# Read the saved game data from the JSON file
def load():
    with open("project/save.json", "r") as file:
       save_data = json.load(file)
       return save_data

# Read and show introduction    
with open("project/intro.txt", "r") as file:
    data = file.read()
    print(data)

# Read and show instructions
with open("project/instructions.txt", "r") as file:
    data = file.read()
    print(data)

# Let the player start a new game or continue a saved game
game_answer = input("New game or continue game? Enter: New / Continue: ")

while game_answer != "New" and game_answer != "Continue":
    game_answer = input("Enter 'New' or 'Continue': ")

if game_answer == "Continue":
    try: 
        saved_game = load()
    except FileNotFoundError: # Start a new game if there is no saved file
        print("No saved game found. Starting a new game.")
        game_answer = "New"

if game_answer == "New": # Ask information if starting a new game
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    answer = ""
    location = milan

elif game_answer == "Continue": 
    name = saved_game["name"]
    age = saved_game["age"]
    answer = saved_game["answer"]
    cheese_ready = saved_game["cheese_ready"]

    inventory = []

    for item in all_items: # Restore the saved inventory and item quantities
        if item.name in saved_game["items"]:
            item.quantity = saved_game["items"][item.name]
            inventory.append(item)
    
    for city in all_locations: # Remove carried items from the cities and restore the saved location
        for item in inventory:
            if item in city.items:
                city.items.remove(item)
        
        if city.name == saved_game["location"]:
            location = city

    print("Saved game loaded.")

if age < 12:
    print("You are a minor, too young to explore Italy alone. The game will shut down.")
else:
    print("\nMain Menu: \nExplore \nTravel \nCollect \nUse \nInventory \nCook \nSave\n")

    player = Player(name, inventory, location)
    print("Hello chef! You are now in " + player.location.name + " and you need to find some ingredients for the wedding menu. Explore this beautiful city.\n")

    command = input("Enter command: ")

    while command != "lopeta": # Repeat the menu until the player quits or completes the game

        if command == "Explore": # give options for different locations
            if player.location == milan: 
                if cooler_bag not in inventory: 
                    print("\nOh, an outside market! That Cooler bag seems nice. Collect it, it's free!")

                elif cooler_bag in inventory and grana_padano not in inventory and answer != "No thank you":
                    print("\nOld woman: Hello! Are you a tourist visiting Milan?")
                    print("\nChef: Oh no, I'm actually a chef. I'm looking for ingredients because I'll be cooking for a wedding in Sicily.")
                    print("\nOld woman: Wow, that's amazing! Would you like to take this Grana Padano? It's typical from here.")
                    print("\nChoose 'Collect' to accept Grana Padano.")
                    print("If you don't want it, type 'No thank you' and press 'Enter'.")

                    answer = input("Type 'Collect' or 'No thank you': ")

                    if answer == "Collect":
                        collect_item(grana_padano, player.location)
                    elif answer == "No thank you":
                        print("\nOld woman: No problem, enjoy your trip.")
                        print("\nYou are ready to leave Milan. Choose 'Travel' to move to Florence.")
                    else:
                        print("Invalid reply.")

                elif cooler_bag in inventory and (grana_padano in inventory or answer == "No thank you"):
                    print("\nYou are ready to leave Milan. Choose 'Travel'.")

            elif player.location == florence:
                if steaks not in inventory:
                    print("\nYou visit a butcher to buy 30 steaks for the wedding.")
                    print("Butcher: I only have 20 steaks ready now. Come tomorrow morning and I will give you the rest of the steaks.")
                    print("\n1. Wait until tomorrow.")
                    print("2. Buy 20 steaks now and buy the rest of the steaks in Rome.")
                    print("3. Look for another butcher.")

                    steaks_choice = input("Choose 1, 2 or 3: ")

                    if steaks_choice == "1":
                        print("\nThe next morning you buy the rest of the steaks.")
                        steaks.quantity = 30
                        collect_item(steaks, player.location)
                    elif steaks_choice == "2":
                        print("\nYou buy 20 steaks. You will have to buy 10 more in Rome.")
                        steaks.quantity = 20
                        collect_item(steaks, player.location)
                    elif steaks_choice == "3":
                        print("\nYou look for another butcher in Florence.\nLuckily, this butcher has the 30 steaks you need.")
                        steaks.quantity = 30
                        collect_item(steaks, player.location)
                    else: 
                        print("\nInvalid choice. Choose 'Explore' to try again.")
                    if steaks in inventory:
                        print("\nYou put the steaks in your cooler bag for your journey.")
                
                elif potatoes not in inventory:
                    print("\nYou need 60 small potatoes for the wedding.")
                    print("\n1. Buy potatoes from a local farmer at the market.")
                    print("2. Buy potatoes from a large supermarket.")

                    potatoes_choice = input("Choose 1 or 2: ")

                    if potatoes_choice == "1":
                        print("\nYou buy 60 potatoes from a local market, supporting local producers.")
                        collect_item(potatoes, player.location)
                    elif potatoes_choice == "2": 
                        print("\nYou buy 60 potatoes from a large supermarket.")
                        collect_item(potatoes, player.location)
                    else: 
                        print("\nInvalid choice. Choose 'Explore' to try again.")
                    if potatoes in inventory:
                        print("\nYou have finished shopping in Florence.")

                else:
                    print("\nShopping in Florence is complete.")
            
            elif player.location == rome:
                if steaks.quantity == 20:
                    print("\nYou visit a butcher in Rome and buy the remaining 10 steaks.")
                    steaks.quantity = 30
                    print("\nYou put them in your cooler bag. You now have 30 steaks.")

                elif pasta not in inventory:
                    print("\nHow will you get pasta for the wedding?")
                    print("\n1. Buy pasta at a local market.")
                    print("2. Buy pasta at a large supermarket.")
                    print("3. Make the pasta yourself.")

                    pasta_choice = input("Choose 1, 2 or 3: ")

                    if pasta_choice == "1":
                        print("\nYou buy pasta from a local producer.")
                        collect_item(pasta, player.location)
                    elif pasta_choice == "2":
                        print("\nYou buy pasta from a large supermarket.")
                        collect_item(pasta, player.location)
                    elif pasta_choice == "3":
                        print("\nYou buy flour at the market and eggs from a local farmer.")
                        collect_item(flour, player.location)
                        collect_item(eggs, player.location)
                        print("You prepare pasta for the 30 guests.")
                        flour.quantity = 0 # Use the flour and 30 eggs to make homemade pasta
                        inventory.remove(flour)
                        eggs.quantity = eggs.quantity - 30
                        collect_item(pasta, player.location)
                        print("\nYou now have 30 eggs left for the carbonara.")
                    else: 
                        print("\nInvalid choice. Choose 'Explore' to try again.")
                    if pasta in inventory:
                        print("\nYou have the pasta ready for the wedding.")  

                elif guanciale not in inventory: 
                    if eggs not in inventory: 
                        print("\nYou visit a local farmer and buy eggs for the carbonara.")
                        collect_item(eggs, player.location)
                    print("\nAt the market, you buy guanciale.")
                    collect_item(guanciale, player.location)
                    print("\nYou put guanciale in the cooler bag.")

                elif not cheese_ready:
                    print("\nChoose 'Use' from the menu to find the cheese.")
                else:
                    print("\nShopping in Rome is complete.")

            elif player.location == naples:
                if rice not in inventory or mushrooms not in inventory:
                    print("\nYou need rice and mushrooms for the wedding risotto.")
                    print("\n1. Visit a market even if it is almost closing time.")
                    print("2. Help at a community kitchen.")
                    print("3. Buy the ingredients in a large shop.")

                    naples_ingredients_choice = input("Choose 1, 2 or 3: ")

                    if naples_ingredients_choice == "1":
                        print("\nA seller offers good unsold rice and mushrooms.")
                        print("You buy them, helping to prevent food waste.")
                        collect_item(rice, player.location)
                        collect_item(mushrooms, player.location)
                        print("\nYou put the mushrooms in your cooler bag.")
                        print("\nYou now have the ingredients for the mushroom risotto.")
                    elif naples_ingredients_choice == "2":
                        print("\nYou help sort donated food at a community kitchen.")
                        print("They give you spare rice and mushrooms to thank you.")
                        collect_item(rice, player.location)
                        collect_item(mushrooms, player.location)
                        print("\nYou put the mushrooms in your cooler bag.")
                        print("\nYou now have the ingredients for the mushroom risotto.")
                    elif naples_ingredients_choice == "3":
                        print("\nYou buy the ingredients in a large shop.")
                        collect_item(rice, player.location)
                        collect_item(mushrooms, player.location)
                        print("\nYou put the mushrooms in your cooler bag.")
                        print("\nYou now have the ingredients for the mushroom risotto.")
                    else: 
                        print("\nInvalid choice. Choose 'Explore' to try again.")
                else:
                    print("\nYour shopping in Naples is complete.")

            elif player.location == taormina:
                if cake not in inventory and cupcakes not in inventory:
                    print("\nYou go to the bakery to get the cake reserved by the wedding couple.")
                    print("Oh no, the baker has been sick, so the cake is not finished!")
                    print("\n1. Help finish the reserved cake.")
                    print("2. Find a ready cake in another bakery.")
                    print("3. Buy 30 cupcakes instead and make a cake with them.")

                    dessert_choice = input("\nChoose 1, 2 or 3: ")

                    if dessert_choice == "1":
                        print("\nYou help the bakery staff finish the cake, avoiding waste.")
                        collect_item(cake, player.location)
                    elif dessert_choice == "2":
                        print("\nYou find another bakery with a ready cake for 30 guests.")
                        collect_item(cake, player.location)
                    elif dessert_choice == "3":
                        print("\nYou buy 30 cupcakes and make a cake with them.")
                        collect_item(cupcakes, player.location)
                    else:
                        print("\nInvalid choice. Choose 'Explore' to try again.")

                    if cake in inventory or cupcakes in inventory:
                        print("\nEverything is ready! Choose 'Cook' to prepare the wedding menu.")
                else:
                    print("\nEverything is ready! Choose 'Cook' to prepare the wedding menu.")

        elif command == "Cook": # Finish the game when the chef reaches Taormina with the dessert
            if player.location == taormina and (cake in inventory or cupcakes in inventory):
                print("\nYou prepare mushroom risotto, carbonara, steaks and potatoes.")
                if cupcakes in inventory:
                    print("\nFor dessert, the guests will eat a cake made of cupcakes.")
                else:
                    print("\nThe wedding cake is served for dessert.")
                print("\nThe wedding couple thanks you and everyone celebrates.")
                print("\nCONGRATULATIONS! YOU SAVED THE ITALIAN WEDDING!")
                break
            else: 
                print("\nYou need to reach Taormina and arrange dessert before cooking.")
                    
        elif command == "Travel": # Command used for moving from one location to another
            travel(player, answer, cheese_ready)
                           
        elif command == "Collect": # Command used to collect the cooler bag in Milan
            if player.location == milan and cooler_bag in player.location.items:
                collect_item(cooler_bag, player.location)
            else:
                print("\nThere are no items to collect here. Keep exploring.")

        elif command == "Use": # Command used to keep, exchange or buy cheese in Rome
            if item_use(player):
                cheese_ready = True

        elif command == "Inventory": # Command used to show all the items and supplies 
            print("\nWelcome to the Inventory.")
            items_list()

        elif command == "Save": # Command used to save the game and the progress
            save(player, age, answer, cheese_ready)

        else:
            print("\nInvalid command.")
    
        print("\nMain Menu: \nExplore \nTravel \nCollect \nUse \nInventory \nCook \nSave\n")
        command = input ("Enter command: ")

    print("Execution stopped.")
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 12:
    print("You are a minor. The game will shut down.")
else:
    print("Hello, "+name+"! \nMain Menu \nWalk \nRun \nTake \nUse \nExchange")

    command = input("Enter command: ")

    while command != "lopeta":
        if command == "Walk":
            print("You are walking.")
        elif command == "Run":
            print("You are running.")
        elif command == "Take":
            print("You took an item.")
        elif command == "Use":
            print("You used an item.")
        elif command == "Exchange":
            print("You exchanged an item.")
        else:
            print("Invalid command.")
    
        print("Main Menu \nWalk \nRun \nTake \nUse \nExchange")
        command = input ("Enter command: ")

    print ("Execution stopped.")
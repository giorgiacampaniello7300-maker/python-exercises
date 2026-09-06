username = input("Enter username: ")
password = input("Enter password: ")

attempts = 0 

while (username != "python" or password != "rules"):
    attempts = attempts + 1
    if attempts == 5: 
        print("Access denied")
        break
    print("Enter the username and password again.")
    username = input("Enter username: ")
    password = input("Enter password: ")
else: 
    print("Welcome")
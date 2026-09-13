airports = {}

instructions = input("Enter an instruction (new, fetch, quit): ")

while instructions != "quit": 
    if instructions == "new":
        ICAO_code = input("Enter ICAO code: ")
        airport_name = input("Enter name of the airport: ")
        airports[ICAO_code] = airport_name
    elif instructions == "fetch":
        ICAO_code = input("Enter ICAO code of the airport: ")
        print(airports[ICAO_code])
    instructions = input("Enter an instruction (new, fetch, quit): ")
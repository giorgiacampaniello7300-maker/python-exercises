names = set()

name = input("Enter a name: ")

while name != "":
    if name not in names:
        print("New name")
    elif name in names:
        print("Existing name")
    names.add(name)
    name = input("Enter a name: ")

for n in names:
    print(n)
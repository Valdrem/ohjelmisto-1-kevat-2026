name = input("Enter the name: ")
names = set()

while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
    name = input("Enter the name: ")

for name in names:
    print(name)


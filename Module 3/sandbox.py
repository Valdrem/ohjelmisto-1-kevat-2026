var1 = "Hello"
var2 = "Bye"

if var1 == "Hello":
    print(f"It's {var1}")
else:
    print(f"It's not {var1}")


money = float(input("How much money do you have?"))

if money >= 5:
    print("You have enough money for a cup of coffee")
    if money >= 10:
        print("You have enough money for 2 cups of coffee")
else:
    print("You have not enough money!")


name = input("What is your name?")

if name.lower() == "valery":
    print("Welcome to Valery!")



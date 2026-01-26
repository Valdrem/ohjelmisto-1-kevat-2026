inches = float(input("Enter length in inches (negative value to quit): "))

while inches > -1:
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters:2.2f} centimeters")
    inches = float(input("Enter length in inches (negative value to quit): "))
else:
    print("Program ended.")

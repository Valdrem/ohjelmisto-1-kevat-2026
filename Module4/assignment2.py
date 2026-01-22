inches = float(input("Enter length in inches (negative value to quit): "))

if inches > -1:
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters:2.2f} centimeters")
else:
    print("Program ended.")
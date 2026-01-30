gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

def gallons_to_liters(litres):
    litres = gallons * 3.785
    return litres

while gallons > 0:
    litres = gallons_to_liters(gallons)
    print(f"{gallons:.1f} American gallons is {litres:.2f} liters.")
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

print("Program finished.")

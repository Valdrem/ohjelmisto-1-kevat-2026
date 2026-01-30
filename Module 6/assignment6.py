import math

diameter_p1 = int(input("Enter the diameter of the first pizza (cm): "))
price_p1 = int(input("Enter the price of the first pizza (euros): "))
diameter_p2 = int(input("Enter the diameter of the second pizza (cm): "))
price_p2 = int(input("Enter the price of the second pizza (euros): "))


def calculate_unit_price(diameter, price):

    diameter_m = diameter / 100
    radius = diameter_m / 2
    final_area = math.pi * (radius ** 2)
    price_per_unit = price / final_area

    return price_per_unit

result_p1 = calculate_unit_price(diameter_p1, price_p1)
result_p2 = calculate_unit_price(diameter_p2, price_p2)


print(f"Unit price of the first pizza: {result_p1:.2f} euros/m²")
print(f"Unit price of the second pizza: {result_p2:.2f} euros/m²")

if result_p1 < result_p2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")


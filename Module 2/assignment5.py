talents = float(input("Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))

total_grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)

total_kg_float = float(total_grams / 1000)
total_kg = int(total_kg_float)
total_grams = total_kg_float - total_kg

print(f"The weigth in modern units: {total_kg} kilograms and {total_grams} grams")
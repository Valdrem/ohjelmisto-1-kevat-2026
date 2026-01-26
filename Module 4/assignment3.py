input_str = input("Enter a number (or press Enter to quit): ")

smallest = ""
largest = ""

while input_str != "":
    # Convert to a float
    current_number = float(input_str)

    # Update largest and smallest
    if largest == "" or current_number > largest:
        largest = current_number

    if smallest == "" or current_number < smallest:
        smallest = current_number

    # Ask for the next number
    input_str = input("Enter a number (or press Enter to quit): ")

# Display results
if largest and smallest != "":
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")











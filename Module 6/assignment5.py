original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_array = []

def filter_even_numbers(filtered_result):

    for number in original_list:
        number = int(number)
        if number % 2 == 0:
            filtered_array.append(number)

filtered_list = filter_even_numbers(original_list)

print(f"Original list: {original_list}")
print(f"List with even numbers only: {filtered_array}")

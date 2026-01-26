number = input("Enter a number: ")
number_list = []

while number != "":
    number = float(number)
    number_list.append(number)
    number = input("Enter a number: ")

number_list.sort(reverse=True)

print(f"The greatest numbers in descending order: ")
for result_nr in number_list:
    print(result_nr)
integer = input("Enter a number: ")
int_list = []

while integer != "":
    integer = int(integer)
    int_list.append(integer)
    integer = input("Enter a number: ")

def sum_of_list():
    array_sum = sum(int_list)
    return array_sum

result = sum_of_list()

print(f"The sum of the numbers in the list is: {result}")







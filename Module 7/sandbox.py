names = ("John", "Mike", "Mike", "John")

print(names[0])
print(names[1])
print(names[-1]) # Prints last name from the list

print(len(names)) # Prints length of the tuple/list


fruits = ["apple", "banana", "cherry"]

(first, second, third) = fruits # Must always correspond total amount of objects in the list

print(first)
print(second)
print(third)


custom = ((1,2,3), (4,5,6), (7,8,9,[10,20,30]))
print(custom)

print(custom[0])
print(custom[2][1]) # Prints second number from  sub tuple in the parent tuple
print(custom[-1][-1][1]) # Prints 20 from the tuple


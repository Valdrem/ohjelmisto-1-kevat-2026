city = input("Enter the name of a city: ")
count = 1
city_list = [city]

for count in range(4):
    city = input("Enter the name of a city: ")
    city_list.append(city)
    count = count + 1

print("\n")
print("The cities you entered: ")
for city_name in city_list:
    print(f"{city_name}")
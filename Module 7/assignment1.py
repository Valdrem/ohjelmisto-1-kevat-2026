month = int(input("Enter the number of a month (1-12): "))

def get_season(month):
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]

    if month in winter:
        print("The season is winter.")
    if month in spring:
        print("The season is spring.")
    if month in summer:
        print("The season is summer.")
    if month in autumn:
        print("The season is autumn.")


if month <= 12 and month >= 1:
    print(f"You entered: {month} ")
    get_season(month)
else:
    print(f"You entered: {month} ")
    print(f"Please enter a number between 1 and 12. ")



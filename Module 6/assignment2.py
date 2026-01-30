import random

custom_dice = int(input("Enter the number of dices:"))

def roll_dice(sides):
    return random.randint(1, custom_dice)

result = roll_dice(custom_dice)

while result < custom_dice:
    print(result)
    result = random.randint(1, custom_dice)

print(result)
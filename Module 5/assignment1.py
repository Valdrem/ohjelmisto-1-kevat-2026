import random

count = int(input("How many dice to roll: "))
dices = []
dice_sum = 0

for count in range(count):
    dice = random.randint(1,6)
    dices.append(dice)
    count = count - 1

for dice in dices:
    dice_sum = dice_sum + dice

print(f"Sum of the dice: {dice_sum}")

import random

def roll_dice():
    return random.randint(1,6)

result = roll_dice()

while result < 6:
    print(result)
    result = random.randint(1, 6)

print(result)
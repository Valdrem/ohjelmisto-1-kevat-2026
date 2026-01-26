import random

random_number = random.randint(1, 10)
user_guess = int(input("Guess a number (1-10): "))

while user_guess != random_number:
    if user_guess < random_number:
        print("Too low")
        user_guess = int(input("Guess a number (1-10): "))
    elif user_guess > random_number:
        print("Too high")
        user_guess = int(input("Guess a number (1-10): "))
else:
    print("Correct")
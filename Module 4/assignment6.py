import random

total_points = int(input("How many points would you like? "))

points_inside_circle = 0
counter = 0

# Condition
while counter < total_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        points_inside_circle = points_inside_circle + 1

    counter = counter + 1

pi_approx = 4 * points_inside_circle / total_points

print(f"Approximation of pi: {pi_approx:1.4f}")
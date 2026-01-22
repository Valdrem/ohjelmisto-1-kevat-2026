import math

loop = 1

while loop < 1000:
    is_zero = loop % 3
    if is_zero == 0:
        print(loop)

    loop = loop + 1

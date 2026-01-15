import random

digit_code3_raw = random.randint(0,9)
digit_code4_raw = random.randint(1,6)

digit_code3 = "".join([str(random.randint(0, 9)) for _ in range(3)])
digit_code4 = "".join([str(random.randint(1, 6)) for _ in range(4)])


print(f"3-digit code: {digit_code3}\n4-digit code: {digit_code4}")
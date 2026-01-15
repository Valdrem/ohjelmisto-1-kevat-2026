from logging import logThreads
from multiprocessing.util import log_to_stderr

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

gram_talents = talents * 20 + 32 + 13.4
gram_lots = lots * 13.3

print(f"The wigth in modern units: {gram_talents}")
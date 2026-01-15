from logging import logThreads
from multiprocessing.util import log_to_stderr

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))


gram = lots * 13.3


print(f"The wigth in modern units: {gram}")
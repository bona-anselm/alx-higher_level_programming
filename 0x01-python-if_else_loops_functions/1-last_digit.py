#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_cpy = number
if number_cpy < 0:
    number_cpy *= -1
ld = (number_cpy % 10)

if ld > 5:
    print(f"Last digit of {number} is {ld} and is greater than 5")
elif ld == 0:
    print(f"Last digit of {number} is {ld} and is 0")
elif ld < 6 and ld != 0:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")

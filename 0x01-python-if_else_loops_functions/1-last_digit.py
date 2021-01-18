#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdg = (number * -1 % 10) * -1
else:
    lastdg = number % 10
if number % 10 > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastdg))
elif number % 10 == 0:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, lastdg))
elif number % 10 < 6 and number != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastdg))

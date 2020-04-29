#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10

if number < 0:
    last = last * -1

if last > 5:
    mensaje = "greater than 5"
elif last == 0:
    mensaje = "0"
else:
    mensaje = "less than 6 and not 0"

print("Last digit of {:d} is {:d} and is {:s}".format(number, last, mensaje))

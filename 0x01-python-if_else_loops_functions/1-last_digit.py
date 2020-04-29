#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10

if number <= 0:
    last = last * -1

mensaje1 = "The last digit of"
if last > 5:
    mensaje = "and is greather than 5"
elif last == 0:
    mensaje = "and is zero"
else:
    mensaje = "and is less than 6 and not 0"

print("{:s} {:d} is {:d} {:s}".format(mensaje1, number, last, mensaje))

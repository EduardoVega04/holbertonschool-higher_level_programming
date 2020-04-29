#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_value = abs(number)
last = abs_value % 10
mensaje = "The last digit of {:d} ".format(number)
mensaje2 = "is {:d} and is ".format(last)

if last > 5:
    print(mensaje + mensaje2 + "greater than 5")
elif last == 0:
    print(mensaje + mensaje2 + "zero")
else:
    print(mensaje + mensaje2 + "less than 6 and not 0")

#!/usr/bin/python3
"""Function that adds two integers. By default, b is 98"""


def add_integer(a, b=98):
    """Our function to add two integers: a and b

    Args:
        a (int): The first parameter
        b (int): The second parameter

    Returns:
        int: The sum of the parameters
        exception: In case there is one or more

    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))

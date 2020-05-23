#!/usr/bin/python3

"""Print a square using the character #"""


def print_square(size):
    """Function to print a square using #

    Args:
        size (int): size of the square

    Returns:
        Nothing. Prints the square using #

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print()

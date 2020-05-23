#!/usr/bin/python3
"""This function will say the input name"""


def say_my_name(first_name, last_name=""):
    """Function to print: My name is <first name> <last name>

    Args:
        first_name (str): The first name
        last_name (str): The last name

    Returns:
        Nothing. It prints: My name is <first name> <last name>

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
"""Function to print a text with 2 new lines after certain characters"""


def text_indentation(text):
    """Function to print the text and two new lines after a '?', '.' and ':'

    Args:
        text (str): The text to print

    Returns:
        Nothing. It prints the text and two new lines after certain characters

    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")

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
    else:
        for i in range(len(text)):
            if text[i] in ['?', '.', ':']:
                print(text[i], end='')
                print('\n')
            else:
                if text[i] == ' ' and text[i - 1] in ['?', ':', '.']:
                    continue
                else:
                    print(text[i], end='')

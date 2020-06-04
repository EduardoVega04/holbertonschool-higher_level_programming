#!/usr/bin/python3
"""Appends text to a file. Create the file if it does not exist"""


def append_write(filename="", text=""):
    """Our function to append text to the file.
       Returns the number of characters writter       
    """
    with open(filename, 'a') as myFile:
        return (myFile.write(text))

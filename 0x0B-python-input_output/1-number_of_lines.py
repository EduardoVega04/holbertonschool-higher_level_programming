#!/usr/bin/python3
"""Prints the number of lines in a text file"""


def number_of_lines(filename=""):
    """Our function that reads the file and does the job"""
    cont = 0
    with open(filename) as myFile:
        while True:
            linesRead = myFile.readline()

            if linesRead == "":
                return cont

            cont += 1

#!/usr/bin/python3
"""Reads and prints to stdout n lines of a text file"""


def read_lines(filename="", nb_lines=0):
    if nb_lines <= 0:
        with open(filename) as myFile:
            print(myFile.read(), end='')
    else:
        cont = 0
        with open(filename) as myFile:
            while True:
                readLines = myFile.readline()

                if not readLines or cont == nb_lines:
                    break

                print(readLines, end="")
                cont += 1

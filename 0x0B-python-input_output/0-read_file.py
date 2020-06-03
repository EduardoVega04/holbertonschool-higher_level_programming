#!/usr/bin/python3
"""Reads an entire file"""


def read_file(filename=""):
    """Reads an entire file at once (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as myFile:
        print(myFile.read())

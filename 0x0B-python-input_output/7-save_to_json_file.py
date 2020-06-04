#!/usr/bin/python3
"""Writes an object to a file, using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Function to serialize and save to file"""
    with open(filename, 'w') as myFile:
        json.dump(my_obj, myFile)

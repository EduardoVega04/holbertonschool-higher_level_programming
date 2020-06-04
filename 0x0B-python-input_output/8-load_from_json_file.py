#!/usr/bin/python3
"""Creates an object from a JSON file"""


import json


def load_from_json_file(filename):
    """Our function"""
    with open(filename, 'r') as myFile:
        return (json.load(myFile))

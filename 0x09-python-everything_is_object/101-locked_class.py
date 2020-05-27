#!/usr/bin/python3
"""Class LockedClass . Low memory cost"""


class LockedClass:
    """Only allows the user to create an attribute called first_name"""

    __slots__ = ["first_name"]

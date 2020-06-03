#!/usr/bin/python3
"""Initialize"""


def inherits_from(obj, a_class):
    """Chacks if the object is an instance of a class
       that inherited (directly of indirectly from the
       specified class
    """
    return (isinstance(obj, a_class) and type(obj) is not a_class)

#!/usr/bin/python3
"""Defines a function is_same_class"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns: If obj is exactly an instance of a_class - True.
             otherwise - False
    """
    return type(obj) is a_class

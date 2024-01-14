#!/usr/bin/python3
"""Defines a class and inherited class check"""

def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited from a_class.

    Args:
    - obj: The object to check.
    - a_class: The specified class.

    Returns:
    - True if obj is instance of a class that inherited from a_class else False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False

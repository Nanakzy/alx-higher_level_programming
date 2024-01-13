#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited (directly or indirectly) from a_class.

    Args:
    - obj: The object to check.
    - a_class: The specified class.

    Returns:
    - True if obj is an instance of a class that inherited from a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

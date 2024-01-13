#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of or if it is an instance of a class
    that inherited from, the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        True if obj is an instance of a_class or its subclasses else False.
    """
    return isinstance(obj, a_class)

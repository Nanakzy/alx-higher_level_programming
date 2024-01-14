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
    if isinstance(obj, a_class):
        return True

    try:
        return issubclass(obj.__class__, a_class)
    except AttributeError:
        return False  # Handle cases where obj is not an instance of a class

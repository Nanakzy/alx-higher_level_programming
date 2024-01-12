#!/usr/bin/python3

def add_integer(a, b=98):
    """ adds 2 integers


    Args:
    a (int or float): the 1st integer
    b (int or float): the 2nd integer (default no 98)

    Returns:
    int: the sum of a and b.

    Raises:
    TypeError if and or b is not an integer or float
    """

    #check if integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    #check if integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

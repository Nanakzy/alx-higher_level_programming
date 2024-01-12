#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)


class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3


def my_mth(self):
    pass

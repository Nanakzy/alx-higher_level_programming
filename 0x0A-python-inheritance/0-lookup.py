def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or hasattr(getattr(obj, attr), '__call__')]

# Test cases
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

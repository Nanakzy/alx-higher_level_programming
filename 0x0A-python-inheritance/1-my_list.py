#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """class inherits from list & provides method for printing sorted list."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)

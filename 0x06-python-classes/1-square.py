#!/usr/bin/python3
"""Module for Square class."""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): Private instance attribute for the size of the square.
    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Returns:
            None.
        """
        self.__size = size

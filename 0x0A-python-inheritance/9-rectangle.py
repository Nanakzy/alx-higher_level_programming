#!/usr/bin/python3
"""Defines a Rectangle class"""


class BaseGeometry:
    """
    Class representing base geometry.
    """

    def area(self):
        """
        Public instance method to calculate the area.

        Raises:
            Exception: area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

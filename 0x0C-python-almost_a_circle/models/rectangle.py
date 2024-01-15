#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either width or height is not an int.
            ValueError: If either width or height <= 0.
            TypeError: If either x or y is not an int.
            ValueError: If either x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self) -> int:
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self) -> int:
        """Get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        """Set the x coordinate of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self) -> int:
        """Get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        """Set the y coordinate of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self) -> int:
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self) -> None:
        """Print the Rectangle using the `#` character taking care of x&y"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            [print(" " * self.x, end="") for _ in range(self.width)]
            print("#" * self.width)

    def update(self, *args: int, **kwargs: int) -> None:
        """Update the Rectangle."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """Return the dictionary representation of a Rectangle."""
        return {
            key[3:]: value
            for key, value in self.__dict__.items()
            if (
                key.startswith("__")
                and key.endswith("__")
                and key != "__nb_objects"
                )
            }

    def __str__(self) -> str:
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

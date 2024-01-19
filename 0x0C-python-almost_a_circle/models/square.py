#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        Raises:
            TypeError: If size is not an int.
            ValueError: If size <= 0.
            TypeError: If either x or y is not an int.
            ValueError: If either x or y < 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self) -> int:
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value: int) -> None:
        """Set the size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs) -> None:
        """update the squre attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self) -> str:
        """Return the print() and str() representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

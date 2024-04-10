#!/usr/bin/python3
"""
This module defines a class Square that represents a square
"""


class Square:
    """
    A class that defines a square.

    Attribuetes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if the current square is equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are equal, False otherwise
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if the current square is not equal to another square

        Args:
            other (Square): The other square to compare

        Returns:
            bool: True if the squares are not equal, False otherwise
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if the current square is greater than another square

        Args:
            other (Square): The other square to compare

        Returns:
            bool: True if the current square is greater, False otherwise
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the current square is greater than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if the current square is less than another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the current square is less than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

#!/usr/bin/python3
"""
This module defines the MagicClass class.
"""
import math


class MagicClass:
    """
    A class that represents a circle.

    Attributes:
        __radius (number): The radius of the circle.
    """
    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance

        Args:
            radius (number): The radius of the circle. Defaults to 0

        Raises:
            TypeError: If the radius is not a number (int or float)
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must bbe a number")
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle
        """
        return 2 * math.pi * self.__radius

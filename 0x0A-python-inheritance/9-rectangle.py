#!/usr/bin/python3
"""
This module includes the class BaseGeometry and its subclass Rectangle.
"""


class BaseGeometry:
    """
    A class featuring public instance methods named 'area' and
    'integer_validator'.
    """
    def area(self):
        """Triggers an exception when invoked."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Verifies that the value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This is a depiction of a rectangle."""
    def __init__(self, width, height):
        """Creation of the rectangle instance."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Provides the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """A casual string representation of the rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

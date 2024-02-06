#!/usr/bin/python3
"""
This module includes the BaseGeometry class and its subclass Rectangle.
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

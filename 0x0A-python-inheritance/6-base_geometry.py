#!/usr/bin/python3
"""
This module includes the class BaseGeometry.
"""


class BaseGeometry:
    """A class featuring a public attribute named 'area'."""
    def area(self):
        """Triggers an exception when invoked."""
        raise Exception("area() is not implemented")

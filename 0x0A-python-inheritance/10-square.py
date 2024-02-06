#!/usr/bin/python3
"""
This module includes the BaseGeometry class and its subclass Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation Of Square"""
    def __init__(self, size):
        """Instantiation Of Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Returns Area Of Square"""
        return self.__size ** 2

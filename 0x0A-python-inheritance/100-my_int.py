#!/usr/bin/python3
"""
holds the class MyInt
"""


class MyInt(int):
    """
    An integer with a rebellious twist, ideal for an opposite day scenario!
    """
    def __new__(cls, *args, **kwargs):
        """Instantiate a new object of the class."""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other

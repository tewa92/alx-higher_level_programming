#!/usr/bin/python3
"""
This module, labeled as '4-print_square', provides a single function called 'print_square'.
"""


def print_square(size):
    """
    This function prints a square composed of '#' characters,
    with each side having a length of 'size'.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")

#!/usr/bin/python3
"""
This module is designed to locate the maximum integer within a list.
"""


def max_integer(list=[]):
    """
    This function aims to identify and retrieve the maximum integer from a list of integers.
    If the list is empty, the function returns None.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

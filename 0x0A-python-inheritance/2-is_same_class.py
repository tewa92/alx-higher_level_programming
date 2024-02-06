#!/usr/bin/python3
"""
This module includes the function called is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Returns true if 'obj' is of the exact class 'a_class';
    otherwise, it returns false.
    """
    return (type(obj) == a_class)

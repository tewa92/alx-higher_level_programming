#!/usr/bin/python3
"""
This module includes the function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    This function returns true if 'obj' is a subclass of 'a_class';
        otherwise, it returns false.
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)

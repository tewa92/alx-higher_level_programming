#!/usr/bin/python3
"""
This module includes the lookup function.
"""


def lookup(obj):
    """Provides a list containing the attributes and methods that are accessible for an object."""
    return dir(obj)

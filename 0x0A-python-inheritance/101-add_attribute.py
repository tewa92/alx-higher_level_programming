#!/usr/bin/python3
"""A module for adding attributes."""


def add_attribute(a_class, name, value):
    """Adds a new attribute to an object if it's feasible."""
    if hasattr(a_class, "__dict__"):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new attribute")

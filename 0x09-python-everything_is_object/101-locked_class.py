#!/usr/bin/python3
"""This class defines a locked object."""


class LockedClass:
    """
    This class restricts the instantiation of new attributes in LockedClass,
    allowing only 'first_name' attributes to be created.
    """

    __slots__ = ["first_name"]

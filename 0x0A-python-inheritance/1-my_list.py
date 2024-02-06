#!/usr/bin/python3
""" The module for managing lists."""


class MyList(list):
    """ inherits from list """
    def print_sorted(self):
        """display sorted lists """
        print(sorted(self.copy()))

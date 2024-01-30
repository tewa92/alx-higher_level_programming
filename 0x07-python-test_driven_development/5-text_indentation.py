#!/usr/bin/python3
"""
This module, titled '5-test_indentation', contains a single function named 'text_indentation
"""


def text_indentation(text):
    """
    This function splits a text into lines based on the characters '?', ':', and '.',
    and adds two new lines after each split.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")

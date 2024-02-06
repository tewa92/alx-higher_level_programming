#!/usr/bin/python3
<<<<<<< HEAD


def read_file(filename=""):
=======
"""
Contains the read_file function
"""


def read_file(filename=""):
    """""reads a text file(UTF8) and prints itstdout"""
>>>>>>> 19279f27c53128cd9296035b156768df92d3adf2
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

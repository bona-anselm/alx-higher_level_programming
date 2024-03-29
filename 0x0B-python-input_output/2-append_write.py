#!/usr/bin/python3
""" module to create a function: write_file """


def append_write(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns
        the number of characters written
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

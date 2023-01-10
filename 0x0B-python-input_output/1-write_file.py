#!/usr/bin/python3
"""def function to write str into a file"""


def write_file(filename="", text=""):
    """open file in write mode"""
    with open(filename, 'w', encoding='utf=8') as fl:
        """output with write file"""
        return fl.write(text)

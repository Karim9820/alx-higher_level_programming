#!/usr/bin/python3
"""
Defines function append_write
"""


def append_write(filename="", text=""):
    """mod returns added chars count"""
    with open(filename, 'a', encoding='utf=8') as fl:
        return fl.write(text)

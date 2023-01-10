#!/usr/bin/python3
"""Defines function to append after each line"""


def append_after(filename="", search_string="", new_string=""):
    """Read file"""
    with open(filename, 'r', encoding='utf=8') as fl:
        lines = []
        while True:
            line = fl.readline()
            if line == "":
                break
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, 'w', encoding='utf-8') as fl:
        fl.writelines(lines)

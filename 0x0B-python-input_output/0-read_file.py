#!/usr/bin/python3
"""Defines a read function"""


def read_file(filename=""):
    """Reads and prints to stdout"""
    with open(filename, "r", encoding="utf=8") as fl:
        print(fl.read(), end="")

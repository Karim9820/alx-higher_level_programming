#!/usr/bin/python3
"""defines a function"""


def inherits_from(obj, a_class):
    """ checks for is subclass"""

    return issubclass(type(obj), a_class)

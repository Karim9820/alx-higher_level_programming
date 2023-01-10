#!/usr/bin/python3
"""initializes function"""


def class_to_json(obj):
    """
    returns
    Dictionary description of object class data
    """
    return obj.__dict__

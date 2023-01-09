#!/usr/bin/python3
"""
Define class
"""


class BaseGeometry:
    """sub"""
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks value"""
        if value is not int:
            raise TypeError("<name> must be an integer")
        """checks value"""
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

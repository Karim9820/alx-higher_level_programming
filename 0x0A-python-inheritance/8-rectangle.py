#!/usr/bin/python3
"""
Defines class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass instance triangle"""
    def __init__(self, width, height):
        """defined values"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

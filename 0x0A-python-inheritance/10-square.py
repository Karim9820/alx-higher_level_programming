#!/usr/bin/python3
"""
import and rep class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(rectangle):
    """def of rep square"""
    def __init__(self, size):
        """inst of square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns area of the square"""
        return self.__size ** 2

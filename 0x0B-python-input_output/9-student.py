#!/usr/bin/python3
"""Defines class Student"""


class Student:
    """instance"""

    def __init__(self, first_name, last_name, age):
        """init instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        """public ins"""
        def to_json(self):
            """Return dict"""
            return self.__dict__

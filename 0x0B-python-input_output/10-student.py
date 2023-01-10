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
        def to_json(self, attrs=None):
            """Return dict
            args:
                attrs (list)
            """
            if (type(attrs) == list and
                    all(type(elmnt) == str for elmnt in attrs)):
                return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
            """ Return:
                    dict
            """
            return self.__dict__

#!/usr/bin/python3
"""Reps class Student"""


class Student:
    """instance"""

    def __init__(self, first_name, last_name, age):
        """init instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        """public def"""

        def to_json(self, attrs=None):
            """Checks attr"""
            if attrs is None:
                return self.__dict__
            new_dict = {}
            for i in attrs:
                try:
                    new_dict[i] = self.__dict__[i]
                except FileNotFoundError:
                    pass
            return new_dict

        def reload_from_json(self, json):
            """replaces  attributes of student"""
            for key in json:
                try:
                    setattr(self, key, json[key])
                except FileNotFoundError:
                    pass


#!/usr/bin/python3
"""
defines func from_json_string
"""
import json


def from_json_string(my_str):
    """
    return
    object rep by json str
    """
    return json.loads(my_str)

#!/usr/bin/python3

"""
defines function 
"""
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as outfile:
        json.dump(my_obj, outfile)

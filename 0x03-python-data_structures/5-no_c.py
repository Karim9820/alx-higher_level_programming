#!/usr/bin/python3

def no_c(my_string):
    newstring = my_string.translate({ord('c'): None})
    newstring = newstring.translate({ord('C'): None})
    return (newstring)

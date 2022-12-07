#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dictnry = {          
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    desm = [roman_dictnry[x] for x in roman_string]
    introm = 0
    for i in range(len(desm)):
        introm += desm[i]
        if desm[i - 1] < desm[i] and i != 0:
            introm -= (desm[i - 1] + desm[i - 1])
        return introm

#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str):
        return 0
    total_digit = 0
    roman_digit = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    for digit in roman_digit.keys():
        if digit in roman_string:
            total_digit += roman_digit[digit]
            roman_string = roman_string.replace(digit, '')

    return total_digit

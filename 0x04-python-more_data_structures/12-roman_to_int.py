#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_digit = {'M': 1000, 'D': 500, 'C': 100,
                   'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    """ prev_value will be use to keep track of
        preview roman number encounted during iterate
    """
    prev_value = 0
    """iterates loop in reverse mod"""
    for i in roman_string[::-1]:
        curr_value = roman_digit[i]
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value
        prev_value = curr_value
    return total

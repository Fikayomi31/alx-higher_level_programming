#!/usr/bin/python3

"""Defines a text indentation function"""


def text_indentation(text):
    """function that prints a text with 2 new lines after 
    each of these characters: ., ? and :
    Args:
        text: text to print
    Raise:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be string')
    
    line = ''

    """Loop over each character in the text"""
    for j in range(len(text)):
        if text[j] == '.' or text[j] == '?' or text[j] == ':':
            """print the current line, followed by two new lines"""
            print(line + text[j])
            print()
        elif text[j] != ' ':
            line += text[j]

    if line:
        print(line)

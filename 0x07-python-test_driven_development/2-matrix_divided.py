#!/usr/bin/python3

"""Function that divide a matrix by an integer"""


def matrix_divided(matrix, div):
    """function that divide element of matrix by a given number

    Args:
        matrix: a list of list of integer of number
        div: the number to divid the matrix
    Raise:
        TypeError: when matrix is not a list of list of number
        TypeError: when row and column is not of the same size
        TypeError: when the div is not a number
        ZeroDivisionError: when the div is 0
    """

    """Check that matrix is a list of lists of integers or floats"""
    if not all(isinstance(row, list) and
               all(isinstance(elem, (int, float)) for elem in row)
               for row in matrix):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """using the first row which is matrix[0] to check it with
    the length wether each length of row is equal to len of matrix[0]
    """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    """Using round to round the new_matrix up to 2"""
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix

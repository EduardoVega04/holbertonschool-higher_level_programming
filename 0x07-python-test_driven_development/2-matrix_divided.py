#!/usr/bin/python3
"""Function to divide the elements of a matrix"""


def matrix_divided(matrix, div):
    """This function will divide the elements of a matrix

    Args:
        matrix (int) or (float): The matrix
        div (int) or (float): The divisor

    Returns
        int or float: The mattrix elements divided by div argument

    """

    if (not isinstance(matrix, list) or
            not all(isinstance(lists, list) for lists in matrix)):
        raise (TypeError
               ('matrix must be a matrix (list of lists) of integers/floats'))

    if not all(all(isinstance
                   (i, (float, int)) for i in row) for row in matrix):
        raise (TypeError
               ("matrix must be a matrix (list of lists) of integers/floats"))

    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return ([list(map(lambda n: round(n/div, 2), i)) for i in matrix])

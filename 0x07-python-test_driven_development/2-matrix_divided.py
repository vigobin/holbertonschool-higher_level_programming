#!/usr/bin/python3
"""Defines a matrix division function. """


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): A of lists of integers or floats.
        div (int/float):The divisor must be a number.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    res_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise TypeError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError("error")
            else:
                inner_list.append(round(items / div, 2))
        res_matrix.append(inner_list)

    return res_matrix

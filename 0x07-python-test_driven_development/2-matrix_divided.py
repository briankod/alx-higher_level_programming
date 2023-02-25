#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The 2-matrix_divided module supplies one function, matrix_divided().
For example,
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


# The isinstance() function returns True if the specified object is of the
# specified type, otherwise False. If the type parameter is a tuple, this
# function will return True if the object is one of the types in the tuple.
# Syntax:
# isinstance(object, type)
# Initialization of variables: None can be used to initialize a variable
# when you don't yet know what value it should have.
# The round() function returns a floating-point number rounded to the
# specified number of decimals. The default number of decimals is 0,
# meaning that the function will return the nearest integer.
# Syntax:
# round(number, digits)
def matrix_divided(matrix, div):
    """Return division of all elements of a matrix"""
    rowsz = None
    e = "matrix must be a matrix (list of lists) of integers/floats"

    # condition to check whether 'matrix' is suitable or not
    if not isinstance(matrix, list):
        raise TypeError(e)
    for elm in matrix:
        # condition to check whether 'elm' is suitable or not
        if not isinstance(elm, list):
            raise TypeError(e)
        # condition to check whether 'val' is suitable or not
        for val in elm:
            if not isinstance(val, int) and not isinstance(val, float):
                raise TypeError(e)

        # The if rowsz is None condition is only true the first time through
        # the loop (i.e., when rowsz has not yet been set), so it sets rowsz
        # to the length of the first row (len(elm)). This ensures that
        # subsequent rows are the same length as the first row.
        if rowsz is None:
            rowsz = len(elm)
        # The elif rowsz != len(elm) condition is only true if the current row
        # has a different length than the first row. In this case, the function
        # raises a TypeError with the message "Each row of the matrix must have
        # the same size", indicating that the matrix is not rectangular and
        # cannot be processed further.
        elif rowsz != len(elm):
            raise TypeError("Each row of the matrix must have the same size")
    # conditions to check whether 'div' is suitable or not
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Round the division to only two decimals
    return([[round(val / div, 2) for val in elm] for elm in matrix])

# A function that divides all elements of a matrix.

#!/usr/bin/python3
"""
This is the 100-matrix_mul module.

The 100-matrix_mul module supplies one function, def matrix_mul().
For example,
>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]
"""


def matrix_mul(m_a, m_b):
    """Return result of multiplication of 2 matrices"""
    # condition to check whether 'm_a' is suitable or not
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    len_a = len(m_a)
    # condition to check whether 'len_a' is suitable or not
    if len_a == 0:
        raise ValueError("m_a can't be empty")
    len_b = None
    for elm in m_a:
        # condition to check whether 'elm' is suitable or not
        if type(elm) is not list:
            raise TypeError("m_a must be a list of lists")
        if len_b is None:
            len_b = len(elm)
            if len_b == 0:
                raise ValueError("m_a can't be empty")
        if len_b != len(elm):
            raise TypeError("each row of m_a must be of the same size")
        # condition to check whether 'val' is suitable or not
        for val in elm:
            if type(val) is not int and type(val) is not float:
                raise TypeError("m_a should contain only integers or floats")
    # condition to check whether 'm_b' is suitable or not
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    # condition to check whether len(m_b) is suitable or not
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    len_elm = None
    for elm in m_b:
        # condition to check whether 'elm' is suitable or not
        if type(elm) is not list:
            raise TypeError("m_b must be a list of lists")
        if len_elm is None:
            len_elm = len(elm)
            if len_elm == 0:
                raise ValueError("m_b can't be empty")
        if len_elm != len(elm):
            raise TypeError("each row of m_b must be of the same size")
        # condition to check whether 'val' is suitable or not
        for val in elm:
            if type(val) is not int and type(val) is not float:
                raise TypeError("m_b should contain only integers or floats")
    # For two matrices to be multiplied, the number of columns in
    # the first matrix must be equal to the number of rows in the
    # second matrix.
    if len_b != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    # Initialize an empty list called result to store the resulting matrix.
    result = []
    # Loop through each row of the first matrix m_a using range(len_a) where
    # len_a is the number of rows in m_a.
    for elm in range(len_a):
        # For each row in m_a, initialize an empty list called x to store the
        # resulting row of the product matrix.
        x = []
        # Loop through each element of the current row of m_a using
        # range(len_elm) where len_elm is the number of elements in
        # the current row.
        for i in range(len_elm):
            # For each element in the current row of m_a, initialize
            # a variable y to store the current sum.
            y = 0
            # Loop through each column of the second matrix m_b using
            # range(len_b) where len_b is the number of columns in m_b.
            for j in range(len_b):
                # For each column in m_b, multiply the current element
                # of the current row of m_a with the current element of
                # the current column of m_b, and add the result to y.
                y += m_a[elm][j] * m_b[j][i]
            # After iterating through all columns of m_b, append y to
            # the list x.
            x.append(y)
        # After iterating through all elements of the current row of m_a,
        # append the resulting row x to the list result.
        result.append(x)
    # After iterating through all rows of m_a, return the resulting matrix
    # result.
    return(result)

# A function that multiplies 2 matrices.

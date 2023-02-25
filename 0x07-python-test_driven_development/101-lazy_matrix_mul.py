#!/usr/bin/python3
"""
This is the 101-lazy_matrix_mul module.

The 101-lazy_matrix_mul module supplies one function, def lazy_matrix_mul().
For example,
>>> print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
[[ 7 10]
 [15 22]]
"""
import numpy as np


# There are three main ways to perform NumPy matrix multiplication:
# np.dot(array a, array b): returns the scalar or dot product of two arrays
# np.matmul(array a, array b): returns the matrix product of two arrays
# np.multiply(array a, array b): returns the element-wise matrix multiplication
# of two arrays
def lazy_matrix_mul(m_a, m_b):
    """Return result of multiplication of 2 matrices by NumPy"""
    return(np.matmul(m_a, m_b))

# A function that multiplies 2 matrices by using the module NumPy.

#!/usr/bin/python3

# Implement a matrix as a nested list (list inside a list).
# Square a Python Number Using the Exponent Operator (**).
def square_matrix_simple(matrix=[]):
    return([[value**2 for value in element] for element in matrix])

# A function that computes the square value of all integers of a matrix.

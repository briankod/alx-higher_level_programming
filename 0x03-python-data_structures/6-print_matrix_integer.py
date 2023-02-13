#!/usr/bin/python3

# The join() method returns a string, which is the concatenation of the
# string (on which it is called) with the string elements of the
# specified iterable as an argument.
# Syntax: str.join(iterable)
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        print(" ".join("{:d}".format(value) for value in element))

# A function that prints a matrix of integers

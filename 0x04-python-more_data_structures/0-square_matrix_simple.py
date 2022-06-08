#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = lambda i: i * i
    return([list(map((square), element)) for element in matrix])

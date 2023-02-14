#!/usr/bin/python3

# This function takes a matrix (i.e., a list of lists) as input and applies
# the map function twice - once to each row of the matrix, and again to each
# element within the row - to compute the square value of each integer.
# The resulting matrix of squared values is returned as a list of lists.
def square_matrix_map(matrix=[]):
    return(list(map((lambda row: list(map((lambda i: i * i), row))), matrix)))

# A function that computes the square value of all integers of a
# matrix using map

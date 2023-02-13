#!/usr/bin/python3

# A particularly clever application of tuple assignment allows us to swap
# the values of two variables in a single statement.
# >>> a, b = b, a
# Both sides of this statement are tuples, but the left side is a tuple of
# variables; the right side is a tuple of expressions. All the expressions
# on the right side are evaluated before any of the assignments.
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))

# switch value of a and b

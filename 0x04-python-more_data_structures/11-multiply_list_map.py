#!/usr/bin/python3

# You can use the map() function to multiply each element in a list.
# The map() function applies a given function to each element of an iterable
# (list, tuple etc.) and returns an iterator containing the results.
# Syntax: map(function, iterable, ...)
# A lambda function is a small anonymous function. A lambda function can take
# any number of arguments, but can only have one expression.
# Syntax: lambda argument(s) : expression
# The lambda function we passed to map gets called with each item in
# the list, multiplies the item by a number and returns the result.
# The last step is to use the list() class to convert the map object to a list.
def multiply_list_map(my_list=[], number=0):
    return(list(map((lambda i: i * number), my_list)))

# A function that returns a list with all values multiplied by a number
# without using any loops.

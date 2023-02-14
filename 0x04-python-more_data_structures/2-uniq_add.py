#!/usr/bin/python3

# Sets are unordered.
# Set elements are unique. Duplicate elements are not allowed.
# The set() builtin creates a Python set from the given iterable.
# Syntax: set(iterable)
# The set() function will help us to convert a list to a set.
def uniq_add(my_list=[]):
    result = 0
    uniq_list = []
    uniq_no = set(my_list)
    for value in uniq_no:
        uniq_list.append(value)
        result += value
    return(result)

# A function that adds all unique integers in a list (only once for
# each integer).

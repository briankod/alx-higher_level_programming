#!/usr/bin/python3
"""Module to find the max integer in a list
"""


# Placeholder for missing values: None can be used as a placeholder when
# a value is missing or not yet known.
def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    # If list is empty, the function returns None. Otherwise, it performs
    # some operation on the list.
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

#!/usr/bin/python3

# The intersection of two sets is the set of all the common elements of both
# the sets. You can use the intersection() method or the '&' operator to find
# the intersection of a Python set.
# >>> first_set.intersection(second_set)
# >>> first_set & second_set
def common_elements(set_1, set_2):
    c_set = set_1 & set_2
    return(c_set)

# A function that returns a set of common elements in two sets.

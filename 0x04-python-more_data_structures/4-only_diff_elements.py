#!/usr/bin/python3

# The symmetric difference between two sets is the set of all the elements that
# are either in the first set or the second set but not in both.
# You have the choice of using either the symmetric_difference() method or
# the '^' operator to do this in Python.
# >>> first_set.symmetric_difference(second_set)
# >>> first_set ^ second_set
def only_diff_elements(set_1, set_2):
    return(set_1 ^ set_2)

# A function that returns a set of all elements present in only one set.

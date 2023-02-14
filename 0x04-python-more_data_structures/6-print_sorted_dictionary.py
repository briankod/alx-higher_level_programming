#!/usr/bin/python3

# The sorted() method sorts iterable data such as lists, tuples,
# and dictionaries. But it sorts by key only.
# The sorted() method puts the sorted items in a list.
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print("{:s}: {}".format(key, a_dictionary[key]))

# A function that prints a dictionary by ordered keys.

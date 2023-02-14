#!/usr/bin/python3

# The items () method in the dictionary is used to return each item in a
# dictionary as tuples in a list. Thus, the dictionary key and value
# pairs will be returned in the form of a list of tuple pairs.
def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}

# A function that returns a new dictionary with all values multiplied by 2

#!/usr/bin/python3

# You can remove a key using the del keyword.
# Syntax: del dict[key]
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return(a_dictionary)

# A function that deletes a key in a dictionary.

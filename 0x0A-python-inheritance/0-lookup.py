#!/usr/bin/python3
"""A function that returns a list object"""


# The dir() method in Python is used to get the list of names of the attributes
# of the passed object in an alphabetically sorted manner,
# When nothing is passed, the method returns back the list of all the local
# attributes.
# Syntax:
# dir(object)
def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return(dir(obj))

# A function that returns the list of available attributes and methods of
# an object

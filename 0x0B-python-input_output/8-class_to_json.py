#!/usr/bin/python3
"""A function that returns the dictionary description with
simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object"""


# obj is a Python object whose attributes we want to convert to a JSON format
# dictionary.
# obj.__dict__ is a built-in Python method that returns a dictionary containing
# the object's attributes and their values.
# This function can be useful if you want to serialize an object in JSON
# format, which requires a dictionary representation of the object's
# attributes.
def class_to_json(obj):
    """returns the dictionary description for
    JSON serialization of an object"""
    return(obj.__dict__)

# A function that returns the dictionary description with simple data
# structure (list, dictionary, string, integer and boolean) for JSON
# serialization of an object.
# Serialization is the process wherein we convert the data type of the raw data
# into a JSON format. With that, we mean to say, that the raw data usually a
# dictionary will now follow the Javascript Object Notation format.

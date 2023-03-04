#!/usr/bin/python3
"""A function that returns the JSON representation of an object (string)"""
# Python has a built-in package called json, which can be used to work with
# JSON data.
# Import the json module
import json


# JSON is a syntax for storing and exchanging data. JSON is text, written with
# JavaScript object notation.
# You can convert Python objects of the following types, into JSON strings:
# dict, list, tuple, string, int, float, True, False, None
# When you convert from Python to JSON, Python objects are converted into the
# JSON (JavaScript) equivalent:
#          Python          JSON
#           dict            Object
#           list            Array
#           tuple           Array
#           str             String
#           int             Number
#           float           Number
#           True            true
#           False           false
#           None            null
# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using
# the json.dumps() method.
def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return(json.dumps(my_obj))

# A function that returns the JSON representation of an object (string)

#!/usr/bin/python3
"""A function that returns an object (Python data structure)
represented by a JSON string"""
import json


# Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return(json.loads(my_str))

# A function that returns an object (Python data structure) represented by a
# JSON string

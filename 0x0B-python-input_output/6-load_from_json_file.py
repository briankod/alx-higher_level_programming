#!/usr/bin/python3
"""A function that creates an Object from a “JSON file”"""
import json


# The main difference between json.load() and json.loads() is in how they
# handle the input data:
# json.load() reads JSON data from a file-like object and parses it into a
# Python object. It takes a file-like object (e.g. a file object opened in
# read mode) as its argument, and it assumes that the input data is already
# in JSON format.
# json.loads() parses a JSON-formatted string into a Python object. It takes
# a string as its argument, and it assumes that the input data is a valid JSON
# string.
def load_from_json_file(filename):
    """creates an Object"""
    with open(filename, 'r', encoding='utf-8') as f:
        return(json.load(f))

# A function that creates an Object from a “JSON file”

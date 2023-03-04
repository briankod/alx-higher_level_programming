#!/usr/bin/python3
"""A function that writes an Object to a
text file, using a JSON representation"""
import json


# f.write(json.dumps(my_obj)) is a Python code that writes a JSON-encoded
# representation of the Python object my_obj to a file.
def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))

# A function that writes an Object to a text file, using a JSON representation

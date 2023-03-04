#!/usr/bin/python3
"""A script that adds all arguments to a
Python list, and then save them to a file"""

# The sys module provides access to some variables used or maintained by
# the Python interpreter and to functions that interact strongly with the
# interpreter.
# The from sys import argv statement is used to import the argv variable from
# the sys module in Python. The argv variable is a list in Python that contains
# the command-line arguments passed to the Python script.
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
try:
    py_list = load_from_json_file(filename)
# The exception handles a case where the file does not exist. The try block
# attempts to load JSON data from the file specified by filename using the
# load_from_json_file function. If this fails due to a FileNotFoundError,
# the py_list variable is set to an empty list.
except FileNotFoundError:
    py_list = []

# The for loop iterates over each command-line argument passed to the script
# (excluding the first argument, which is the name of the script itself). For
# each argument, it appends the argument to the py_list variable.
for elm in argv[1:]:
    # The append() method adds an item to the end of the list.
    # Syntax:
    # list.append(item)
    py_list.append(elm)
save_to_json_file(py_list, filename)

# A script that adds all arguments to a Python list, and then save them to
# a file

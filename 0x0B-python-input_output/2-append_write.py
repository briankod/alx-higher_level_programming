#!/usr/bin/python3
"""A function that appends a string at the end of a text file (UTF8)"""


# 'a' - Open a file for appending at the end of the file without truncating it.
# Creates a new file if it does not exist.
def append_write(filename="", text=""):
    """returns the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as f:
        return(f.write(text))

# A function that appends a string at the end of a text file (UTF8) and returns
# the number of characters added

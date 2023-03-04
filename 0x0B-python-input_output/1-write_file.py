#!/usr/bin/python3
"""A function that writes a string to a text file (UTF8)"""


# write(s)	Writes the string s to the file and returns the number of
# characters written. This function writes a fixed sequence of
# characters to a file.
# f.write() is a method in Python used to write data to a file. The
# method writes a string or bytes object to a file object, and returns
# the number of characters or bytes written.
# 'w' - Open a file for writing. Creates a new file if it does not exist
# or truncates the file if it exists
def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, 'w', encoding='utf-8') as f:
        return(f.write(text))

# A function that writes a string to a text file (UTF8) and returns the
# number of characters written

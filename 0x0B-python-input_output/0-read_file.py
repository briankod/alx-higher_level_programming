#!/usr/bin/python3
"""A function that reads a text file (UTF8)"""


# open(), a built-in function that opens a file and allows your program to
# use it and work with it.
# Syntax:
# open(<file>, <mode>)
# 'file': relative or absolute path to the file(including the extension)
# 'mode': a string(character) that indicates what you want to do with the file
# In addition to the main parameters, open() can also take a number of optional
# parameters, including buffering, encoding, errors, newline, closefd and
# opener.
# We usually use a relative path. Example
# open("names.txt"), the relative path is "names.txt"
# Modes available are: Read ("r"), Append ("a"), Write ("w"), Create ("x"), ...
# Example of a context manager used to work with files:
# with open("<file>", "<mode>") as <var>, where 'with' is a keyword and 'var'
# is a variable that will be used to refer to the file object.
# Unlike open() where you have to close the file with the close() method, the
# with statement closes the file for you without you telling it to.
def read_file(filename=""):
    """prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        # read the file line by line using a for loop and print each line
        # to the console.
        for line in f:
            print(line, end="")

# A function that reads a text file (UTF8) and prints it to stdout

#!/usr/bin/python3

# https://youtu.be/sugvnHA7ElY
# Before executing a program, the Python interpreter assigns the name of the
# python module into a special variable called __name__. Depending on whether
# you are executing the program through command line or importing the module
# into another module, the assignment for __name__ will vary.
# The general syntax to import and call a function from a separate file is
# below:
# from function_file import function_name
# function_name(arguments)
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

# A program that imports the function def add(a, b): from the file add_0.py and
# prints the result of the addition 1 + 2 = 3

#!/usr/bin/python3

# sys.argv is a list in Python that contains all the command-line
# arguments passed to the script.
# With the len(sys.argv) function, you can count the number of arguments.
# The enumerate() function takes a collection (e.g. a tuple) and returns
# it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.
# Syntax: enumerate(iterable, start). By default, start is zero.
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    print("{:d} {:s}{:s}".format(n - 1, "argument" if n <= 2 else "arguments",
                                 "." if n == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))

# A program that prints the number of and the list of its arguments

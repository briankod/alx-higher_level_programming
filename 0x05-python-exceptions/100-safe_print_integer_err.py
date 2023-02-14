#!/usr/bin/python3

# Multiple exceptions Syntax:
# Except(Exception1, Exception2,…ExceptionN) as e:
# You can print to stderr in Python using either the sys.stderr.write()
# function or the print() function with the file parameter set to
# sys.stderr. Here's the syntax for both options:
# Using sys.stderr.write():
# import sys
# sys.stderr.write("Error message\n")
# Using print():
# import sys
# print("Error message", file=sys.stderr)
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return False
    else:
        return True

# A function that prints an integer.
# Returns True if value has been correctly printed (it means the
# value is an integer) Otherwise, returns False and prints in
# 'stderr' the error precede by 'Exception:'

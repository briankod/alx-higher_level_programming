#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value), end="\n")
    except (ValueError, TypeError):
        return False
    else:
        return True

# A function that prints an integer with "{:d}".format().
# Returns True if value has been correctly printed (it means the
# value is an integer) Otherwise, returns False

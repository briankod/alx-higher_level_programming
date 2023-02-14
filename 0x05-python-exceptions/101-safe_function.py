#!/usr/bin/python3

# *args allows us to pass a variable number of non-keyword arguments
# to a Python function.
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None

# A function that executes a function safely.
# You can assume fct will be always a pointer to a function
# Returns the result of the function,
# Otherwise, returns None if something happens during the function and
# prints in stderr the error precede by Exception:

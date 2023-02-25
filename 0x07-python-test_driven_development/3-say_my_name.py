#!/usr/bin/python3
"""
This is the 3-say_my_name module.

The 3-say_my_name module supplies one function, say_my_name().
For example,
>>> say_my_name("Hiro", "Nakamura")
My name is Hiro Nakamura
"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first name> <last name>' """
    # condition to check whether 'first_name' is suitable or not
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    # condition to check whether 'last_name' is suitable or not
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    # This code uses the format() method to print a formatted
    # string containing the values of two variables first_name
    # and last_name. The {} placeholders in the string are
    # replaced with the corresponding variable values in the
    # order they are passed to the format() method.
    print("My name is {} {}".format(first_name, last_name))

# A function that prints My name is <first name> <last name>

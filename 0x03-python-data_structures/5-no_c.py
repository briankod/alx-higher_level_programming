#!/usr/bin/python3

# Append character to string through using + operator to
# concatenate a string and a character and return a new string.
def no_c(my_string):
    # initialization of string to ""
    replacement = ""
    # traverse in the string
    for value in my_string:
        if value != 'c' and value != 'C':
            replacement += value
    return(replacement)

# A function that removes all characters c and C from a string

#!/usr/bin/python3

# Python dictionaries consist of key:value pairs, allowing you to search
# for a key and return its value. Python dictionaries are created using
# curly braces, {}.
# Here, we will use the dict.keys() method to get a list-like
# object containing the keys of the dictionary, and use the len()
# function to determine the number of keys.
def number_keys(a_dictionary):
    key_list = a_dictionary.keys()
    return(len(key_list))

# A function that returns the number of keys in a dictionary.

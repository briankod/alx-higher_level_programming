#!/usr/bin/python3

# Use 'dict[key] = value' to Add Items to a Python Dictionary
# We were able to easily append a new key:value pair to a dictionary
# by directly assigning a value to a key that didn’t yet exist.
# When we try to add an item to a dictionary when the item’s key
# already exists, the dictionary simply updates. This is because
# Python dictionaries require the items to be unique, meaning that
# it can only exist once.
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return(a_dictionary)

# A function that replaces or adds key/value in a dictionary.

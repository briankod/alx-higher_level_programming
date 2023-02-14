#!/usr/bin/python3

# Python list() function takes any iterable as a parameter and
# returns a list.
def best_score(a_dictionary):
    if not a_dictionary:
        max_ = None
    if a_dictionary:
        # Initialize max_ to the first key in the dictionary
        max_ = list(a_dictionary.keys())[0]
        # Iterate over the keys in the dictionary
        for key in a_dictionary:
            # If the value of the current key is greater
            # than the value of max_ , update max_ .
            if(a_dictionary[key] > a_dictionary[max_]):
                max_ = key
    # Return the key with the maximum value
    return(max_)

# A function that returns a key with the biggest integer value.

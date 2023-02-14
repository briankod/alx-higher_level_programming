#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i, value in enumerate(my_list):
        if value == search:
            new_list[i] = replace
    return(new_list)

# A function that replaces all occurrences of an element by another
# in a new list

#!/usr/bin/python3

# The del operator removes the item or an element at the specified
# index location from the list, but the removed item is not
# returned, as it is with the pop() method.
def delete_at(my_list=[], idx=0):
    if my_list:
        if 0 <= idx < len(my_list):
            del my_list[idx]
    return my_list

# A function that deletes the item at a specific position in a list

#!/usr/bin/python3

# The copy() method returns a shallow copy of the list
# The copy() method returns a new list. It doesn't modify the original list.
# Syntax: new_list = list.copy()
def new_in_list(my_list, idx, element):
    i = 0
    a = my_list.copy()
    while(i < len(a)):
        if idx < 0 or idx >= len(a):
            return(my_list)
        elif i == idx:
            a[i] = element
            return(a)
        i += 1

# A function that replaces an element in a list at a specific position
# without modifying the original list (like in C)

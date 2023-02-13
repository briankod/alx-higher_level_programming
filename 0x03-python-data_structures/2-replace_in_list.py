#!/usr/bin/python3

# With the while loop we can execute the set of statements as long as a
# condition is true. Otherwise, it will exit from the Python while loop.
# We also used + operator to increment the i value (i += 1). After
# increment, the process repeats until the condition results False.
def replace_in_list(my_list, idx, element):
    i = 0
    while(i < len(my_list)):
        if idx < 0 or idx >= len(my_list):
            return(my_list)
        elif i == idx:
            my_list[i] = element
            return(my_list)
        i += 1

# A function that replaces an element of a list at a specific
# position (like in C).

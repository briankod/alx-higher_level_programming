#!/usr/bin/python3

# When a return statement is used in a function body, the execution
# of the function is stopped. If specified, a given value is
# returned to the function caller.
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return
    else:
        return(my_list[idx])

# A function that retrieves an element from a list like in C

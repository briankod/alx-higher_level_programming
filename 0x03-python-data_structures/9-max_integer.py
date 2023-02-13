#!/usr/bin/python3

# To find the largest number in a list in Python:
# 1. Set the first element as the largest number candidate.
# 2. Loop through the list of numbers.
# 3. Update the largest number candidate if a number is greater than it.
def max_integer(my_list=[]):
    if len(my_list) == 0:
        max_ = None
    if len(my_list) > 0:
        max_ = my_list[0]
        for value in my_list:
            if(value > max_):
                max_ = value
    return(max_)

# A function that finds the biggest integer of a list

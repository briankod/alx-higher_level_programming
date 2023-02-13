#!/usr/bin/python3

# You can simply use % Modulus operator to check divisibility.
# For example: n % 2 == 0 means n is exactly divisible by 2 and
# n % 2 != 0 means n is not exactly divisible by 2.
# The append method receives one argument, which is the value you want to
# append to the end of the list.
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for value in my_list:
            if value % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
    return(new_list)

# A function that finds all multiples of 2 in a list
# Return a new list with True or False, depending on whether the integer
# at the same position in the original list is a multiple of 2
# The new list should have the same size as the original list

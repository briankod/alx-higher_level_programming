#!/usr/bin/python3

# my_list[::1] would return the entire list from beginning to end.
# If we, instead, stepped using a value of -1, then we would
# traverse the list from the last item to the first.
def print_reversed_list_integer(my_list=[]):
    if my_list:
        a = my_list[::-1]
        for value in a:
            print("{:d}".format(value), end="\n")

# A function that prints all integers of a list, in reverse order

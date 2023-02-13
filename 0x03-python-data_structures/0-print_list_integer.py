#!/usr/bin/python3

# The output will be printed in separate lines because \n has been
# added to the end of each line
def print_list_integer(my_list=[]):
    for value in my_list:
        print("{:d}".format(value), end="\n")

# A function that prints all integers of a list

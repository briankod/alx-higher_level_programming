#!/usr/bin/python3

# The range() function returns a sequence of numbers, starting
# from 0 by default, and increments by 1 (by default), and
# stops before a specified number
# Syntax: range(start, stop, step)
# try-except block Syntax:
# try:
#     <do something>
# except Exception:
#     <handle the error>
# The idea of the try-except block is this:
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# It may be combined with the else and finally keywords.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the
# result of the try- and except blocks.
# The way you handled the error here is by handing out a pass.
# Pass: The pass statement in Python is used when a statement or
# a condition is required to be present in the program, but we
# don’t want any command or code to execute. It’s typically
# used as a placeholder for future code.
# To count in a for loop manually:
# 1. Initialize a count variable and set it to a number.
# 2. Use a for loop to iterate over a sequence.
# 3. On each iteration, reassign the count variable to its
# current value plus N.
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            pass
    print()
    return (count)

# A function that prints x elements of a list.
# x represents the number of elements to print
# x can be bigger than the length of my_list

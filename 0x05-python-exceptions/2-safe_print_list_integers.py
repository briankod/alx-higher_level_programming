#!/usr/bin/python3

# Continue: The continue statement in Python is used to skip the remaining
# code inside a loop for the current iteration only.
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return (count)

# A function that prints the first x elements of a list and only integers.

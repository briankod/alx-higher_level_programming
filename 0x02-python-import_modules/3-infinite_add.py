#!/usr/bin/python3

# Casting(specifying a type on to a variable) is done using constructor
# functions.Includes: int(), float() and str().
if __name__ == "__main__":
    from sys import argv
    sum_all = 0
    for i in argv[1:]:
        sum_all += int(i)
    print("{:d}".format(sum_all))

# A program that prints the result of the addition of all arguments

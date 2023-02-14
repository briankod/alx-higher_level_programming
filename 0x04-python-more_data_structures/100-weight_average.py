#!/usr/bin/python3

# The formula for finding the weighted average is the sum of all
# the variables multiplied by their weight, then divided by the
# sum of the weights.
def weight_average(my_list=[]):
    if not my_list:
        return 0
    if my_list:
        x = 0
        y = 0
        for tuple_ in my_list:
            x += (tuple_[0] * tuple_[1])
            y += tuple_[1]
        return (x / y)

# A function that returns the weighted average of all integers
# tuple (<score>, <weight>)

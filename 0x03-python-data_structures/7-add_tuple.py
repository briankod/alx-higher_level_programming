#!/usr/bin/python3

# When creating a tuple with one item, add a comma at the end.
# The len function can be used to get the length of a tuple.
# Accessing items in a tuple works similar to a list, using indexes.
# A python tuple can be reassigned with a different value.
# To join two or more tuples you can use the + operator.
# Unpacking a tuple means splitting the tuple’s elements into individual
# variables. Example x, y = (1, 2) The left side: x, y is a tuple of two
# variables x and y. The right side is also a tuple of two integers 1 and 2.
def add_tuple(tuple_a=(), tuple_b=()):
    zero_tuple = (0, )
    i = len(tuple_a)
    j = len(tuple_b)
    if i > 2:
        w = tuple_a[0]
        x = tuple_a[1]
        tuple_a = (w, x)
    if j > 2:
        y = tuple_b[0]
        z = tuple_b[1]
        tuple_b = (y, z)
    if i < 2:
        while(i < 2):
            tuple_a = tuple_a + zero_tuple
            i += 1
    if j < 2:
        while(j < 2):
            tuple_b = tuple_b + zero_tuple
            j += 1
    a1, a2 = tuple_a
    b1, b2 = tuple_b
    a = a1 + b1
    b = a2 + b2
    new_tuple = (a, b)
    return(new_tuple)

# A function that adds 2 tuples

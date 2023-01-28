#!/usr/bin/python3

# Prints numbers from 0 to 99 separated by a comma, followed by a space
# in ascending order with two digits.The last number should be followed
# by a new line.
for i in range(0, 99):
    print("{:02d}".format(i), end=', ')
print("{:02d}".format(i + 1))

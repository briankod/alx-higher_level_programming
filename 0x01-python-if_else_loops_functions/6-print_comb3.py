#!/usr/bin/python3

# Prints all possible different combinations of two digits. Numbers must be
# separated by a comma, followed by a space. Print only the smallest
# combination of two digits. Numbers should be printed in ascending order,
# with two digits. The last number should be followed by a new line.
for i in range(0, 8):
    for j in range(i + 1, 10):
        print("{:d}{:d}".format(i, j), end=", ")
print("{:d}{:d}".format(i + 1, j))

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    print("{:d} {:s}{:s}".format(n - 1, "argument" if n <= 2 else "arguments",
                                 "." if n == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))

# A program that prints the number of and the list of its arguments

#!/usr/bin/python3

# The quit() and exit() are used interchangeably
# break statement terminates the current loop and resumes
# execution at the next statement
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = ["+", "-", "*", "/"]
    from calculator_1 import add, sub, mul, div
    calcs = [add, sub, mul, div]
    for i, s in enumerate(ops):
        if argv[2] == s:
            print("{} {} {} = {}".format(a, s, b, calcs[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)

# A program that imports all functions from the file calculator_1.py
# and handles basic operations.

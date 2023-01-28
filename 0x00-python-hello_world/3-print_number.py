#!/usr/bin/python3

# When using f-Strings to display variables, you only need to specify
# the names of the variables inside a set of curly braces {}. And at
# runtime, all variable names will be replaced with their respective values.
# Format codes
# Syntax: {[argument_index_or_keyword]:[width][.precision][type]}
number = 98
print(f"{number:d} Battery street")

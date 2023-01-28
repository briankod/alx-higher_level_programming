#!/usr/bin/python3

# range() function returns a sequence of numbers, starting from 0 by default,
# and increments/steps by 1 (by default), and stops before a specified number.
# Syntax: range(start, stop, step)
# The ord() function returns the number representing the unicode code of a
# specified character. Syntax: ord(character)
for i in range(ord('a'), ord('z') + 1):
    print("{:c}".format(i), end="")

# The format() method formats the specified value(s) and insert them inside the
# string's placeholder{}. Inside the placeholders you can add a formatting type
# to format the result. Syntax: string.format(value1, value2...)
# :c Converts the value into the corresponding unicode character
# Prints the ASCII alphabet, in lowercase.
# end Parameter with No Space and No Newline. Syntax: print(end="")

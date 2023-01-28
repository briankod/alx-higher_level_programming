#!/usr/bin/python3

# Prints the ASCII alphabet, in lowercase, not followed by a new line,
# except the letters q and e.
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print("{:c}".format(i), end="")

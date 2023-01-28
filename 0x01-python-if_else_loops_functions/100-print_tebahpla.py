#!/usr/bin/python3

# Prints the ASCII alphabet, in reverse order, alternating lowercase and
# uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format((c - (ord('a') - ord('A'))) if c % 2 else c), end='')

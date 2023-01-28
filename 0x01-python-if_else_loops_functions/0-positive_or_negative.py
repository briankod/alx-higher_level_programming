#!/usr/bin/python3

# The random module gives access to various useful functions and one
# of them being able to generate random numbers, which is randint().
import random
# Syntax : randint(start, end)
number = random.randint(-10, 10)
# Print whether the number stored in the variable number is positive,
# zero or negative.
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")

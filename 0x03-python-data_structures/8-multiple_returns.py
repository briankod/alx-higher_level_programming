#!/usr/bin/python3

# Python Inline If-Else
# Syntax: some_expression if condition else other_expression
def multiple_returns(sentence):
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)

# A function that returns a tuple with the length of a string and
# its first character.

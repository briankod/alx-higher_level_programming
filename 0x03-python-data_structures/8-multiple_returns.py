#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        first  = None
    if len(sentence) > 0:
        first = sentence[0]
    return(length, first)

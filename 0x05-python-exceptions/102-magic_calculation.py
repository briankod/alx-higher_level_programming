#!/usr/bin/python3

# Break:A break statement in Python alters the flow of a loop by
# terminating it once a specified condition is met.
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return (result)

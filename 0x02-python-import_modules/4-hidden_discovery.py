#!/usr/bin/python3

# The dir() method returns a list of valid attributes of the object.
if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):
        if i[:2] != "__":
            print("{:s}".format(i))

# A program that prints all the names defined by the
# compiled module hidden_4.pyc

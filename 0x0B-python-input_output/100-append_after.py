#!/usr/bin/python3
"""A function that inserts a line of text to a file, after
each line containing a specific string (see example)"""


# search_string and new_string are strings, this code can be used to search
# for a specific string in the lines of a file and append a new string to
# each line that contains the search string.
def append_after(filename="", search_string="", new_string=""):
    """appends a line of new string after the line
    where the searched string is found"""
    with open(filename, 'r', encoding='UTF8') as f:
        # The readlines() function in Python takes a text file as input
        # and stores each line in the file as a separate element in a list.
        tmp = f.readlines()

    with open(filename, 'w', encoding='UTF8') as f:
        for line in tmp:
            if search_string in line:
                line = line + new_string
            f.write(line)

#  A function that inserts a line of text to a file, after each line
# containing a specific string (see example)

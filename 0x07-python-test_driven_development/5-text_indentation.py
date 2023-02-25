#!/usr/bin/python3
"""
This is the 5-text_indentation module.

The 5-text_indentation module supplies one function, text_indentation(text).
For example,
>>> text_indentation("Common burger ingredients: buns, beef and ketchup.")
Common burger ingredients:
<BLANKLINE>
buns, beef and ketchup.
<BLANKLINE>
"""


# The function initializes a flag variable to 0. This flag variable will be
# used to keep track of whether we are currently in a whitespace or
# non-whitespace section of the text.
# The function then iterates over each character in the input text. If the
# flag is 0 (i.e., we are currently in a whitespace section), the function
# skips over any spaces it encounters and sets the flag to 1 when it
# encounters the first non-space character.
# If the flag is 1 (i.e., we are currently in a non-whitespace section), the
# function checks whether the current character is a '.', '?' or ':'. If it
# is, it prints out the character, followed by a newline character ('\n'),
# and sets the flag back to 0. If it is not, it simply prints out the
# character without any modification.
# The function continues this process until it has processed all characters in
# the input text.
def text_indentation(text):
    """Prints a text with 2 new lines after given characters(.),(?)and(:)"""
    # condition to check whether 'text' is suitable or not
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for chr in text:
        if flag == 0:
            if chr == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if chr == '?' or chr == '.' or chr == ':':
                print(chr)
                print()
                flag = 0
            else:
                print(chr, end="")

# A function that prints a text with 2 new lines after each of these
# characters: ., ? and :

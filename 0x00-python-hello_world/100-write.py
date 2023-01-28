#!/usr/bin/python3

# sys module provides access to some variables used or maintained by the
# interpreter and to functions that interact strongly with the interpreter.
# Includes: sys.stdin, sys.stdout, sys.stderr, sys.exit([arg]), e.t.c
# File objects used by the interpreter for standard input, output and errors:
# stdin is used for all interactive input (including calls to input());
# stdout is used for the output of print() and expression statements and
# for the prompts of input();
# The interpreter’s own prompts and its error messages go to stderr.
import sys
# To print to standard error in Python sys.stderr.write() method is used.
sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
# sys.exit([arg])
# Raise a SystemExit exception, signaling an intention to exit the interpreter
sys.exit(1)

# echo $? is used to check the status/return code of last executed command.
# If status shows '0' then command was successfully executed and
# if shows '1' then command was a failure.

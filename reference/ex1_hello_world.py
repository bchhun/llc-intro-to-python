from __future__ import print_function

import sys

if sys.version_info > (3,0):
    raw_input = input

# raw_input takes whatever you pass it and puts it in a variable
name = raw_input("Please enter your name so we can greet you: ")

print("Hello " + name)

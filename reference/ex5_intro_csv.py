# -*- coding: utf-8 -*-
"""
Python is said to come with 'batteries included' – a number of utility libraries available with the standard installation

In this exercise, we'll open a CSV file with one of the built-in utilities and read some data from a row.
"""

from __future__ import print_function
import csv
import os

#
# In order to read a CSV file. First, we need to open the file (the reader needs file input).
# When you open a file using the "with" keyword, it creates a new block for you and the file will
# be automatically closed for you when the block is done executing.
#
with open(os.path.join(os.pardir, 'exercises', 'llc-chapters.csv')) as chapters_file:

    #
    # Then we use the DictReader to parse that file. It will read the first row, and expose each subsequent row as a
    # dictionary where the column header is the key for the corresponding value in that row.
    #
    reader = csv.DictReader(chapters_file)

    #
    # As long as there are rows left to read, you can call `.next()` and get a dictionary for that row
    #
    row1 = reader.next()
    print(row1)
    # {'City': 'Vancouver', ' Chapter Lead(s)': ' Meghan', ' Province': ' BC'}

    row2 = reader.next()
    print(row2)
    # {'City': 'Calgary', ' Chapter Lead(s)': ' Darcie ', ' Province': ' AB'}

    #
    # Since we've got a dictionary, we can print out the value by accessing it with a valid key
    #
    print(row1['City'])
    # Vancouver

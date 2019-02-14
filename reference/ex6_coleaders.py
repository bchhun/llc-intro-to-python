
from __future__ import print_function
import csv
import os


with open(os.path.join(os.pardir, 'exercises', 'llc-chapters.csv')) as csv_file:
    csv_data = csv.DictReader(csv_file)

    count = 0
    for row in csv_data:
        if row['Chapter Lead(s)'].find("&") >= 0:
            count += 1
            print(row['City'])

    print(str(count) + " cities have co-leads")

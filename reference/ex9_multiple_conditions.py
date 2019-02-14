# -*- coding: utf-8 -*-

"""
In a press release, you're trying to pique journalists' interest. One popular topic in programming is digital literacy
for youth. LLC hosts many events throughout the year under 'Kids Learning Code' and 'Girls Learning Code' banners.

In order to count all these events, we'll need to use the boolean `or` operator we saw this morning
"""

from __future__ import print_function
import csv
import os


with open(os.path.join(os.pardir, 'exercises', 'llc-workshop-data.csv')) as workshop_file:

    reader = csv.DictReader(workshop_file)

    #
    # We can find either term if we combine the searches with `or`
    #
    count = 0
    for row in reader:
        name = row['Event Name']
        if name.find('Kids Learning Code') >= 0 or name.find('Girls Leaning Code') >= 0:
            count += 1

    print(count)
    # 609

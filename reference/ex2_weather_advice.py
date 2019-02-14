from __future__ import print_function

import sys

if sys.version_info > (3,0):
    raw_input = input

weather = raw_input("What is the weather? (cold, raining, etc.): ")

if weather == "cold":
    print("Wear a sweater!")
elif weather == "raining":
    print("Bring an umbrella")
else:
    print("Dress normally :)")

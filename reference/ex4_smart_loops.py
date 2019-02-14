# Here is a list of many numbers
# Use variables, for loops, and if statements to complete the following tasks

from __future__ import print_function

numbers = [2,14,144,62,1729,44,101,210,6,12,33,550,1001,11,142,674,
           37,45,167,764,999,3,66,174,982,112,245,501,63,91]

# Task 1: count how many numbers are less than 50

count_under_50 = 0
for number in numbers:
    if number < 50:
        count_under_50 = count_under_50 + 1

print('There are '+ str(count_under_50) + ' numbers under 50 in this list.')

# Task 2: count how many numbers are greater than 500 and less than 1000
count_over_500_less_1000 = 0
for number in numbers:
    if number > 500 and number < 1000:
        count_over_500_less_1000 = count_over_500_less_1000 + 1

print('There are '+ str(count_over_500_less_1000) + ' numbers between 500 and 1000 in this list.')

# Bonus: count how many numbers are odd
count_odd_numbers = 0
for number in numbers:
    if number % 2 != 0:
        count_odd_numbers = count_odd_numbers + 1

print('There are '+ str(count_odd_numbers) + ' odd numbers in this list.')

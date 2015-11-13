#!/usr/bin/python

sum_numbers = 0

for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_numbers += i

print sum_numbers
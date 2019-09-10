#!/usr/bin/env python

# print(a list using list comprehension)

l = ['a', 'b', 'c']

print(" ".join([i for i in l]))

import string
print(string.join([i for i in l], " "))

# Print a list with commas
print(string.join([i for i in l], ", "))


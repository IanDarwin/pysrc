#!/usr/bin/env python

# print a list using list comprehension

list = ['a', 'b', 'c']

print list

print(" ".join([i for i in list]))

import string # so we can use class method string.join
print(string.join([i for i in list], " "))

# Print a list with commas
print(string.join([i for i in list], ", "))


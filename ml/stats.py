#!/usr/bin/env python3

''' Trivial examples of numpy and scipy basic statistics '''

prices = [87, 113, 373, 240]
print("Data is", prices)

import numpy

print("Mean is", numpy.mean(prices))
# 203.25
print("Median is", numpy.median(prices))
# 176.5

# print("Mode is", numpy.mode(prices))
# Exception: no such method

from scipy import stats

print("Mode is", stats.mode(prices))

#!/usr/bin/env python3

''' Trivial examples of basic statistics (mean, median, mode)
using plain python, using numpy, and using scipy.
'''

prices = [87, 113, 373, 240]
print("Data is", prices)

# We can get the mean/average easily
print("Mean is", sum(prices)/len(prices))

# Or we can use numpy to compute it.
import numpy
print("Mean is", numpy.mean(prices))
# 203.25

# Getting the median would be harder by hand, easier with numpy
print("Median is", numpy.median(prices))
# 176.5

# Same for the mode:

# print("Mode is", numpy.mode(prices))
# Exception: no such method

from scipy import stats

print("Mode is", stats.mode(prices))

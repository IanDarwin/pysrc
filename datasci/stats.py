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

# Getting the median would be harder by hand, easier with numpy
print("Median is", numpy.median(prices))

# Ditto for the mode, so we use scipy:

from scipy import stats

print("Mode is", stats.mode(prices))

# For more on statistics for ML in Python, see
# https://www.w3schools.com/python/python_ml_standard_deviation.asp

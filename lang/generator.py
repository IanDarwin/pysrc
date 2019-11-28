#!/usr/bin/env python

# A 'generator' is an object that can be used with the
# built-in next function, e.g., next(generator)
# A generator is usually used to control a 'for' loop
# Particularly useful when the result is too big to fit in memory.

prices = (100, 200, 300)
discount = 0.25

# This is the generator object - it does not compute any values until
# you pass it into next().
totals = (price - (price * discount) for price in prices if price>100)

print("Use generator in a for loop")
for t in totals:
	print(t)

# What it prints:
# 150
# 225

# The generator has been "used up" so we have to re-create it
totals = (price - (price * discount) for price in prices if price>100)

print("Use generator 'manually', doing what the 'for' loop did internally
print(next(totals))
print(next(totals))
print(next(totals))
print(next(totals))

# What it prints:
# 150
# 225
# StopIteration

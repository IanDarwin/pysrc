#!/usr/bin/env python

# A 'generator' is an object that can be used with the
# built-in next function, e.g., next(generator)
# A generator is usually used to control a 'for' loop
# Particularly useful when the result is too big to fit in memory.

prices = [200, 400, 500]
fee = 20

# This is the generator object - it does not compute any values until
# you call next().
totals = (price - fee for price in prices)

# What is it?
print("Totals is of",type(totals))

print("Use generator in a for loop")
for t in totals:
	print(t)

# The generator has been "used up" so we have to re-create it
totals = (price - fee for price in prices)

print("Use generator 'manually', doing what the 'for' loop did internally")
print(next(totals))
print(next(totals))
print(next(totals))
# This would throw a StopIteration exception to indicate that the iteration is used up.
# print(next(totals))

# Different brackets, different result
totals = [price - fee for price in prices]
print("Totals is of",type(totals))

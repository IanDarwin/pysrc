#!/bin/env python

# Show doc string on a function and on a class

def x():
	"""This is the documentation on function 'x'."""
	return 42

print(x)

print(x())

print(x.__doc__)

class y:
	"""This is the documentation for class 'y'."""
	def __init__(self, name):
		"""And this, the docco for 'y' constructor."""
		self.name = name

print(y)

print(y("Ian"))

print(y.__doc__)

print(y.__init__.__doc__)

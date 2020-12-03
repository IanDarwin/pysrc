#!/usr/bin/env python

# To create our own iterator requires two methods: __iter__ and __next__
class x:
	list = ['Uno', 'Dos', 'Tres' ]
	def __init__(self):
		self.i = 0;
	def __iter__(self):
		return self
	def __next__(self):
		if self.i >= len(self.list):
			raise StopIteration
		self.i += 1
		return self.list[self.i - 1]

obj = x()

for var in obj:
	print(var)

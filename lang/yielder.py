#!/usr/bin/env python

# Create a function that returns an interator (using yield)
def squareList(l):
	for i in l:
		yield i*i

iter = squareList(range(1,5))
print iter

for s in iter:
	print s


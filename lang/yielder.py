#!/usr/bin/env python

# Create a function that returns an interator (using yield)
def squareList(l):
	for i in l:
		yield i*i

iter = squareList(range(1,5))
print("Iter = ", iter)

print("iter next() = ", next(iter))
print("iter.next() = ", next(iter))

print("Resetting generator")
iter = squareList(range(1,5))

# Iteration (normal):
for s in iter:
	print(s)

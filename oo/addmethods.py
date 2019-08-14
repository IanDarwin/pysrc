#!/usr/bin/env python

class X:
	foo = 0
	def __init__(self, foo = 0):
		self.foo = foo

x = X()
setattr(x, 'bar', lambda: x.foo + 1)
print x.bar()

x = X(42)
setattr(x, 'bar', lambda: x.foo + 1)
print x.bar()

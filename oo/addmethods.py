#!/usr/bin/env python

class X:
	foo = 0
	def __init__(self, foo = 0):
		self.foo = foo

# Add a method to one instance:
x1 = X()
setattr(x1, 'bar', lambda: x1.foo + 1)
print(x1.bar())

# Add the same method to the class, so all
# instances will have it.
X.zee = lambda x: x.foo + 2
x2 = X(42)
print(x2.zee())

print(x1.zee())

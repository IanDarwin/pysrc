#!/usr/bin/env python

# see if __ private vars are accessible

class X:
	__val = 'base'

if __name__ == '__main__':

	x = X()

	mesg = 'belong to us'

	# Python's pseudo-private variables are implemented just by mangling the name to hide them,
	# putting _CLASSNAME before them. You can see it in the dir(x) output:
	print(dir(x))
	# Backdoor if you know the trivial mangling algorithm:
	print('All your %ss' % x._X__val, 'are', mesg, "!")

	# This won't compile
	# X.__val

	# SO: private vars ARE accessible outside - but only by the back door.
	# Java has a backdoor too - using member.setPrivate(false) in the Reflection API.

# Single-underscore "private" or "hidden" class members are NOT hidden.

class A:
	def __init__(self):
		pass
	def _foo(self):
		print("Foo on you!");

a = A();
a._foo();


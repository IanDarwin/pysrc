#!/usr/bin/env python

# Quick demo of ignoring an exception

try:
	x = Float("Moo")
except:
	pass
print("Don't have a cow")

#!/usr/bin/env python

# demonstrate Python's try/except/finally (like Java's try/catch/finally)

try:
	print("Trying")
	raise IndexError
	print("Should not get here!") # Causes compiler warning
except IndexError:
	print("Caught expected IndexError:")
except "Erised":
	print("Magical Error: Caught str 'Erised': should not happen.")
finally:
	print("In finally, Doing boring clean-up")

print("All done")

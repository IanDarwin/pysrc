#!/usr/bin/python -u

# demonstrate Python's variant of try/catch/finally

try:
	print "Trying"
	raise IndexError
	print "Should not get here!"
except IndexError:
	print "Caught expected IndexError:"
except "Erised":
	print "Strange Error: Caught Erised: should not happen."
finally:
	print "In finally, Doing boring clean-up"

print "All done"

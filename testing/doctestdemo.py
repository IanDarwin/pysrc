#!/usr/bin/env python

""" This is a doc string just to demonstrate 'doctest'
'doctest' checks that document string fragments pasted from interactive Python still work.
See https://docs.python.org/3/library/doctest.html

You can run this directly in Python due to the __main__ at the bottom.

>>> mystring = 'Hello world'
>>> mystring.upper()
'HELLO WORLD'
"""

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	print("No news is good news!")

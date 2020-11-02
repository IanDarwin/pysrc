#!/usr/bin/env python

""" This is a doc string just to demonstrate 'doctest'
You can run this as a Python script due to the __main__ at the bottom.
DocTest checks that your documents pasted from interactive Python still work.
See https://docs.python.org/3/library/doctest.html

>>> mystring = 'Hello world'
>>> mystring.upper()
'HELLO WORLD'

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

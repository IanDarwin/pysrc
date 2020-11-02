#!/usr/bin/env python

""" This is a doc string, taken from the slide in lt1905add.
You can run this as a Python script due to the __main__ at the bottom.
DocTest checks that your documents pasted from interactive Python still work.
See https://docs.python.org/3/library/doctest.html

>>> word = 0x10203040
>>> xfmt = '{0:x}'
>>> xfmt.format(word)       
'10203040'

>>> # | bitwise or - turn bits on
>>> xfmt.format(word | 0b11110000)
'102030f0'

>>> # & bitwise or - masking (turn bits off)
>>> xfmt.format(word & 0xff)
'40'

>>> # ~ negate - oft used w/ masking
>>> xfmt.format(word & ~0xff)
'10203000'

>>> # bit shifting - each <<1 doubles
>>> xfmt.format(word << 1)
'20406080'

>>> # bit shifting - each >>1 halves
>>> xfmt.format(word >> 1)
'8101820'
>>> 
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

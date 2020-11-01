#!/usr/bin/env python

# Bit-twiddling operators

word = 0x10203040
xfmt = '{0:x}'
print('Original: ',xfmt.format(word))
# | bitwise or - turn bits on
print('|: ', xfmt.format(word | 0b11110000))
# & bitwise or - masking (turn bits off)
print('&: ', xfmt.format(word & 0xff))
# ~ negate - oft used w/ masking
print('~: ', xfmt.format(word & ~0xff))
# bit shifting - each <<1 doubles
print('<<: ', xfmt.format(word << 1))
# bit shifting - each >>1 halves
print('>>: ', xfmt.format(word >> 1))



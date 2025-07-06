#!/usr/bin/env python

import itertools

# Print all the "words" makeable from these letters

characters = ['c', 'o', 'd', 'e']
characters = [ 'a','b','c','d','e','f']

for word in itertools.permutations(characters):
    print(''.join(word))

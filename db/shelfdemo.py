#!/usr/bin/env python

import shelve

shelf = shelve.open('shelfdemo')

dict = { 'alpha':1, 'beta':2, 'gamma':3 }
for (k,v) in dict.items():
	shelf[k] = v

print "Shelf Before: ", shelf

shelf.close()
del shelf

sh2 = shelve.open('shelfdemo')

print "Shelf reloaded", sh2

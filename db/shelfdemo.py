
import shelve

shelf = shelve.open('scan.shelf')

dict = { 'alpha':1, 'beta':2, 'gamma':3 }
for (k,v) in dict.items():
	shelf[k] = v

print "Shelf Before: ", shelf

shelf.close()
del shelf

sh2 = shelve.open('scan.shelf')

print "Shelf reloaded", sh2

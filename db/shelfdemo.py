
import shelve

shelf = shelve.open('scan.shelf')

dict = { 1:'alpha', 2:'beta', 3:'gamma' }
for (k,v) in shelf.keys():
	shelf[k] = v

print "Dict:", dict
print "Shelf Before: {",
for (k,v) in shelf.keys():
	print k, v
print "}"

shelf.close()

sh2 = shelve.open('scan.shelf')

print "Shelf2"
for (k,v) in sh2.keys():
	print k, v

#!/usr/bin/env python

# add up running totals in a dictionary
# case study: printer accounting

fakedata={'ian':4, 'robin':1, 'ian':6, 'unknown':1}
pages={}

for (username,pages) in fakedata.items():
	n = pages.setdefault(username, 0)
	n += numpages
	pages[username] = n

for (u,qty) in pages.items():
	print "chargeforpages.py", u, qty

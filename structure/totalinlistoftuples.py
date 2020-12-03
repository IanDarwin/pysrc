#!/usr/bin/env python

# add up running totals in a list of tuples
# case study: printer accounting

fakedata=[('ian',4), ('robin',1), ('ian',6), ('unknown',1)]
pages={}

for (username,numpages) in fakedata:
	# Despite the name, setDefault gets a value if present
	n = pages.setdefault(username, 0)
	n += numpages
	pages[username] = n

for (u,qty) in pages.items():
	print("chargeforpages.py", u, qty)

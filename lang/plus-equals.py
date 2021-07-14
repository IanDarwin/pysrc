#!/usr/bin/env python3

# why += etc?

count = 1
count += 2			# this line...
print(count)

count = 1
tmp = count + 2		# replaces these
count = tmp			# two lines.
print(count)

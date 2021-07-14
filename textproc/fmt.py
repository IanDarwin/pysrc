#!/usr/bin/env python

import sys

linelength = 72
out = ""

for line in sys.stdin.readlines():
	if len(line) == 0:	# null line
		print("")
		if out:
			print(out)
			out = ""
	else:
		for word in line.split():
			out += word + ' '
			if (len(out) > linelength):
				print(out)
				out = ""
if out:
	print(out)

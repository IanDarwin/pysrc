#!/usr/bin/env python

# read well from a file

filename = "/tmp/id"

try:
	with open(filename) as input:
		for line in input:
			print(line.rstrip())
except IOError as e:
	print("I/O Error reading", e.args, file=sys.stderr)

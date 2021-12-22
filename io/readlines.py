#!/usr/bin/env python

# read multiple lines from stdin

import sys

for line in sys.stdin:
	print(line[:-1])	# Cheesy rstrip()

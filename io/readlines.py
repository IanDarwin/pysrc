#!/usr/bin/env python

# read multiple lines from stdin

import sys

line="line";

for line in sys.stdin:
	print(line[:-1])

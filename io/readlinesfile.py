#!/usr/bin/env python

# read multiple lines from named file

import sys

line="line";

for line in open("/etc/passwd"):
	print(line[:-1])

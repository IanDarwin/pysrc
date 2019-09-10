#!/usr/bin/env python

# The "rdist" program copies files remotely; unfortunately it translates
# spaces in filenames to the hideosity "\040" on the remote site.
# This generates a shell script to repair them. Note: if you have
# directories with spaces, this becomes a two-pass algorithm; you can
# just run the script twice if you're prepared to ignore errors.
# Use as: ls | fix.py | sh 
# Optionally: sh -x instead of sh, and/or sh 2>/dev/null

import sys

for line in sys.stdin:
	line = line[:-1]
	print("mv '" + line + "' '" + \)
	line.replace(r'\040',"_") + "'" 

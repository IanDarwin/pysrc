#!/usr/bin/env python

# Show regex in action (regex = generic name; python package is re)
# Note use of "raw strings" (r'...') to avoid excess backslashing

import re

line = "Alpha 12.3 Gamma OO.O Omega AA.A"

if re.match(r"^\w+\s+\d+(\.\d+)?\D+$",line):
        print "Found"
else:
	print "Not found"

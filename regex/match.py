#!/usr/bin/env python

import re

''' Find match up to first comma '''

s = 'Forescore and seven years ago, our fathers brought forth...'

# match up to ","
m = re.match(r'^.*,', s)

# print(just what matched)
print(m.group(0))

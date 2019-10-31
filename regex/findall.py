#!/usr/bin/env python

import re

'''Find all occurrences of a pattern in a string'''

s = 'Forescore and seven years ago, our fathers brought forth...'

print(re.findall(r'\w+', s))

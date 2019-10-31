#!/usr/bin/env python

''' Show splitting a string on a regex '''

import re

s = 'Forescore and seven years ago, our fathers brought forth...'

print(re.split(r'\W+', s))

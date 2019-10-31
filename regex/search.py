#!/usr/bin/env python

''' Show matcher groups in action '''

import re

s = 'Forescore and seven years ago, our fathers brought forth...'

m = re.search(r'go', s)

print(m.group(0))

print(m.start(), m.end())

print(s[m.start() : m.end()])

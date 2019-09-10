#!/usr/bin/env python

import re

s = 'Forescore and seven years ago, our fathers brought forth...'

print(re.findall(r'\w+', s))

#!/usr/bin/env python

import re

'''Find all occurrences of a pattern in a string'''

s = "Once, upon a midnight dreary, as I pondered, weak, and weary..."

print(re.findall(r'[^\w](a\w?)', s))

#!/usr/bin/env python

import re

s = 'Forescore and seven years ago, our fathers brought forth...'

# mangle it to 'FXXescXXe and seven years ago, our fathers brought fXXth...'
# just to show how sub works

print re.sub(r'or', r'XX', s)

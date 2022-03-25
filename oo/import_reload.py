'''
Show how to reload an imported module.
Don't ask me why it's so verbose - used to be a builtin.
'''
def dump():
	print(dir(math))
	print(id(math))

import math
dump()

# Re-load the math module
import sys, importlib
importlib.reload(sys.modules['math'])
dump();

# The cheesy way (may be less efficient; gets a new id()
del math
import math
dump()

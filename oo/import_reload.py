'''
Show how to reload an imported module.
'''
def dump():
	print(dir(math))
	print(id(math))

import math
dump()

# Re-load the math module
import importlib
importlib.reload(math)
dump();

# The cheesy way (may be less efficient; gets a new id()
del math
import math
dump()

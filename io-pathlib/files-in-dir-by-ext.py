#!/usr/bin/env python

import sys
from pathlib import Path

# The directory we will look in, and what to look for
dir_path = Path.home() / 'pytalk'

if not dir_path.exists():
	print("You can't run this example as you don't have ~/pytalk.")
	sys.exit(1)

ext = ".odp"

# The traditional way
import os
files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) \
        if os.path.isfile(os.path.join(dir_path, f)) and f.endswith(ext)]
print(files)

# The pathlib way
from pathlib import Path
files = list(Path(dir_path).glob("*"+ext))
print(files)

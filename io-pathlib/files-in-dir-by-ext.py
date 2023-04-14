#!/usr/bin/env python

# The directory we will look in, and what to look for
dir_path = "/home/ian/pytalk"
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

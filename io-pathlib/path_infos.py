#!/usr/bin/env python

from pathlib import Path

path = Path("/etc/locate.rc") # Exists on most Unix, Linux, macOS

print('path:', path)
print('type(path):', type(path))
print('str(path):', str(path))
print('path.exists():', path.exists())
print('path.is_file():', path.is_file())
print('path.is_dir():', path.is_dir())
print('path.absolute():', path.absolute())
print('path.parent:', path.parent)
print('path.name:', path.name )
print('path.stem:', path.stem)
print('path.suffix:', path.suffix)

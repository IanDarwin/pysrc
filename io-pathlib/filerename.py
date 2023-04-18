#!/usr/bin/env python

# create, rename, read back, and delete a file

from pathlib import Path

old = Path("x")
new = Path("y")

old.write_text("This is a silly file!")

old.rename(new)

print("Read from renamed file:", new.read_text())

new.unlink()

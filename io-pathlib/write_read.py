#!/usr/bin/env python

# Simple reading/writing with pathlib

from pathlib import Path

pt = Path("/tmp/ian.adoc")

pt.write_text("= My Exciting Article About Pathlib\n");
with pt.open(mode="a") as file:
    file.write(":author: Ian Darwin\n")
print(pt.read_text())

pb = Path("/tmp/ian.bin")
pb.write_bytes(b'\1\2\3\4\5')
print(pb.read_bytes()) # b'\x01\x02\x03\x04\x05'

# clean up
pt.unlink()
pb.unlink()

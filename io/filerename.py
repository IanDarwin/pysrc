#!/usr/bin/env python

# rename a file

import os

open("/tmp/x","w").close();

os.rename('/tmp/x', '/tmp/y')

os.system("ls /tmp");

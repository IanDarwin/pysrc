#!/usr/bin/env python

# Create a bytearray and write it as raw data

# bytearray constructor takes an iterable of ints
ba=bytearray([1,2,3])

print(ba)
# Should print: bytearray(b'\x01\x02\x03')

bfile=open("./bfile", 'wb');
n = bfile.write(ba)
if (n == len(ba)):
	pass
else:
	raise IOException("Did not write entire file")

bfile.close();

# Now in the terminal do this (on Unix):
# od -bc /tmp/bfile
# If all's well, output should look like this:
# 0000000  001 002 003                                                    
#          001 002 003                                                    
# 0000003
# indicating that the 1, 2, and 3 got written as bytes.


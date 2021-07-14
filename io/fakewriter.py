#!/usr/bin/env python

# fake output class - works due to duck-typing. 

import sys

class fakewriter:
	def __init__(self):
		self.buf = ''
		self.stdout = sys.stdout
	def print(self, stuff):
		self.buf += stuff
	def write(self, stuff):
		self.buf += stuff
	def flush(self):
		self.stdout.write(self.buf)
	def dump(self):
		print("Contents of", self, ":")
		print(self.buf)

print("Hello")
out = fakewriter()
out.write("Hello")
out.dump()

sys.stdout = fakewriter()
print("Neat")

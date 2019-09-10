#!/usr/bin/env python

# partly-written fake output class. 
# DO NOT COMMIT until can assign to sys.out and have "print" work.

class fakewriter:
	buf = ''
	def write(self, stuff):
		self.buf += stuff
	def dump(self):
		print("Contents of", self, ":")
		print(self.buf)

print("Hello")
out = fakewriter()
out.write("Hello")
out.dump()

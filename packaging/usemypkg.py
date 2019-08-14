''' Trivial demo of using a class from a package. '''

import mypkg.demo

print "Hello from main"
d = mypkg.demo.demo();
d.demo()
print "Goodbye from main"

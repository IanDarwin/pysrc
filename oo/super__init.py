# Demo of using super() to call superclass constructor
# Note that you don't need to pass "self" when using super,
# as you do when calling by class name.

class A:
	"A class"
	def __init__(self, name):
		self.greeting = "Hello"
		self.name = name

class B(A):
	def __init__(self, name):
		A.__init__(self, name) # must pass self
		super().__init__(name) # don't pass self

ab = B("Ian")

print(ab.greeting, ab.name)

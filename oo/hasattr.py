class A:
	classdata = "some class stuff here"
	def __init__(self, data):
		self.data = data
	def display(self):
		print(self.data)

a = A(22)
print(dir(a))
print(hasattr(a, 'classdata'), hasattr(a, 'display'), hasattr(a, '__del__'))
a.display()


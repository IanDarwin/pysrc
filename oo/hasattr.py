class A:
	classdata = 15
	def __init__(self): self.data = 22
	def display(self): print(self.data)

a = A()
print(dir(a))
print(hasattr(a, 'classdata'), hasattr(a, 'display'), hasattr(a, '__del__'))


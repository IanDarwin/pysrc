class xlist(list):
	def push(self, x):
		self.append(x)

x=xlist()
x.append(12)
print(x)
# should print([12])
x.push(42)
print(x)
# should print([0, 42])


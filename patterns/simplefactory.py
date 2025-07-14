# Simplest factory

class Cheese:
	def __init__(self, style):
		self.style = style

	def __str__(self):
		return f'This is a fine {self.style} Cheese'

id = "Cheese"
constructor = globals()[id]
instance = constructor('Cheddar')

print(instance)

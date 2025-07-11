# Ascertain if static methods can be seen outside the class.

class StaticsVisible:

	@staticmethod
	def now():
		return "today";

	def __init__(self):
		pass

print(StaticsVisible.now()); # Un-indented so not part of the class

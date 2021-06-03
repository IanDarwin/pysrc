"""
Defines the information about a person
"""


class Person:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def get_name(self):
		return self.firstname + ' ' + self.lastname


ian = Person('Ian', 'Darwin')
print(ian.get_name())

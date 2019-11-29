class Person:
	''' Defines the information about a person '''
	def __init__(self, firstname, lastname):
		self.firstname = firstname;
		self.lastname = lastname;

	def getName(self):
		return self.firstname + ' ' + self.lastname;

ian = Person('Ian', 'Darwin')
print(ian)

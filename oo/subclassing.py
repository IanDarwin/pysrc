class Person:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def get_name(self):
		return self.firstname + ' ' + self.lastname

class Customer(Person):
	def __init__(self, company, *nameargs):
		self.company  = company
		super().__init__(*nameargs)

	def get_name(self):
		return "{} {} at {}".format(self.firstname, self.lastname, self.company)

ian = Customer('Rejminet Group Inc.', 'Ian', 'Darwin')
print(ian.get_name())

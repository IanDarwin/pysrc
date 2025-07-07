class BankAccount:
	def __init__(self, bal):
		self.bal = bal
 
	# Overload the + operator: + maps to magic __add__ method
	def __add__(self, other):
		return BankAccount(self.bal + other.bal)

	# stringify
	def __str__(self):
		return "BankAccount: Balance: " + str(self.bal)

acct1 = BankAccount(100)
acct2 = BankAccount(250)
 
print(acct1 + acct2)


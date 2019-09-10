class BankAccount:
     def __init__(self, num=0, balance=0.0): # defines constructor
         self.balance = balance
     def deposit(self, amount):
         self.balance += amount

acct=BankAccount(90210) # calls constructor
print(acct.balance)
acct.deposit(2500)
print(acct.balance)


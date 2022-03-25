#!/usr/bin/env python

# use the BankAccount class in a different file.

from constructor import BankAccount

acct=BankAccount(90210) # calls constructor
print(acct.balance)
acct.deposit(2500)
print(acct.balance)

print(vars(acct))

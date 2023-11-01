#!/usr/bin/env python

# Match statement can end with EITHER a non-literal name
# (which creates a variable of that name) OR an underscore.

bow = input("Enter name: ")

match name := bow.lower():
	case 'atlantic':
		print("Atlantic")
	case 'pacific' | 'indian':
		print('Big')
	case fred:
		print("Other is ", fred)
#	 case _:
# 		print("Default")

print("Thanks for playing.")

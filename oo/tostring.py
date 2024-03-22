#!/usr/bin/env python

# using vars() to print an object is kinda messy,
# so you may want to use a __str__ function instead.

class Trip:
	"Class represents a Trip from one city to another."
	def __init__(self, depCity, arrCity):
		self.depCity = depCity
		self.arrCity = arrCity
		print(self.__doc__)
		
	''' The equivalent of toString in Java and like languages '''
	def __str__(self):
		return f"Trip from {self.depCity} to {self.arrCity}"

trip = Trip('Toronto', 'Jamaica')

print(trip)


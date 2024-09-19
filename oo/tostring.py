#!/usr/bin/env python

# using vars() to print an object is kinda messy,
# so you may want to use a __str__ function instead.

class Trip:
	"""The Trip class represents one journey from one city to another."""
	def __init__(self, dep_city, arrival_city):
		self.dep_city = dep_city
		self.arrival_city = arrival_city

	''' The equivalent of toString in Java and like languages '''
	def __str__(self):
		return f"Trip from {self.dep_city} to {self.arrival_city}"

	# Not customary! Just to show the __doc__ attribute
	def help(self):
		print(self.__doc__)

trip = Trip('Toronto', 'Jamaica')

print(trip)

trip.help();


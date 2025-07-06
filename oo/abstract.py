from abc import ABC, abstractmethod

class Abstract(ABC):
	@abstractmethod
	def my_am(self):
			""" Abstract """
			print("Abstract method invoked") # Ignored, not usable.

f = Abstract()	# won't compile, abstract.
f.my_am() 

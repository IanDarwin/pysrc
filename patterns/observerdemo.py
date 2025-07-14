# Simple demo of Observer pattern
# Example could be made simpler by up-folding subclasses.

from abc import ABC, abstractmethod

# DEFINE OWN OBSERVER FRAMEWORK

class Subject(ABC):
	def __init__(self):
		self.observers = []

	def register_observers(self, *observers):
		for observer in observers:
			self.observers.append(observer)

	def notify(self, data):
		for obs in self.observers:
			obs.update(data)

class Observer(ABC):

	@abstractmethod
	def update(self, data):
		pass

# SPECIALIZE THE FRAMEWORK: Cooking School

class ChefSchool(Subject):
	def __init__(self):
		super().__init__()
		self.recipes = []

	def add_recipe(self, recipe):
		self.recipes.append(recipe)
		self.notify(recipe)

class Chef(Observer):
	def __init__(self, name):
		super().__init__()
		self.name = name

	def update(self, recipe):
		print(f"Chef {self.name} got recipe {recipe}")

# MAIN

if __name__ == '__main__':
	school = ChefSchool()
	obs_gordon = Chef("Gordon Ramsay")
	obs_jamie = Chef("Jamie Oliver")
	school.register_observers(obs_gordon, obs_jamie)
	school.add_recipe("Pasta Sauce with Pickled Herring")
	school.add_recipe("Peanut Butter and Tuna Fish Sandwich")

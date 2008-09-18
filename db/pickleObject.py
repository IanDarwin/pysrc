#!/usr/bin/env python

import pickle

youWantThisToBlowUp = False

class Person:
	def __init__(self, name, id=1, meaning=42):
		self.name = name
		self.id = id
		self.meaning = meaning
	def __str__(self):
		return 'Person(%s,%d,%d)' % (self.name, self.id, self.meaning)

file = open('pickleObject.dat', 'w')
pickle.dump(Person('Fred'), file)
file.close();

if youWantThisToBlowUp:
	del Person

file2 = open('pickleObject.dat');
fred2 = pickle.load(file2)
print fred2

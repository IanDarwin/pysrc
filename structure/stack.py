#!/usr/bin/env python

class Stack:
	def __init__(self, list=[]):
		self.list = list
	def push(self, item):
		return self.list.append(item)
	# pop is provided in list
	def __unicode__(self):
		return `self.list`
	def __getattr__(self, attrname):
		return getattr(self.list, attrname)

s = Stack([1,2,3]);
print s
s.push(42)
print s
print s.pop()
print s.list.pop()
print s


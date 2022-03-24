'''
Attempts to implement these definitions from Python documentation:

hashable

	An object is hashable if it has a hash value which never changes
	during its lifetime (it needs a __hash__() method), ...
	[Note that this is different from Java, and probably C#]
	... and can be
	compared to other objects (it needs an __eq__() or __cmp__()
	method). Hashable objects which compare equal must have the same
	hash value.

	Hashability makes an object usable as a dictionary key and a set member,
	because these data structures use the hash value internally.

	All of Python's immutable built-in objects are hashable, while no
	mutable containers (such as lists or dictionaries) are. Objects
	which are instances of user-defined classes are hashable by
	default; they all compare unequal (except with themselves), and
	their hash value is derived from their id().

immutable

	An object with a fixed value. Immutable objects include numbers,
	strings and tuples. Such an object cannot be altered. A new object
	has to be created if a different value has to be stored. They play
	an important role in places where a constant hash value is needed,
	for example as a key in a dictionary.

By those definitions, this class is hashable but NOT immutable.
Could make it the latter by renaming name to __name throughout.
'''

class Demo:
	__id = 0
	name = None

	def __init__(self, id, name):
		self.__id = id
		self.name = name

	def __hash__(self):
		return self.__id

	def __eq__(self, other):
		if not other.__class__ == self.__class__:
			return False
		if self.__id != other.__id:
			return False
		return True

# main
d1 = Demo(24, 'Guido')
d2 = Demo(24, 'Guido')

# See if you expect and can explain the following outputs:
print(d1 is d2)
print(d1 == d2)
print(d1.__hash__() == d2.__hash__())
print(d1 == "This parrot")


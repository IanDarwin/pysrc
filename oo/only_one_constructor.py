'''
Python only allows one method of a given name, including constructors
If you have two 'def' statements with the same name (regardless of parameters),
the second one will 'win' by over-writing (replacing) the first one.
'''
class ConstrDemo:
	def __init__(self, arg1):
		print("One-arg constructor")
	def __init__(self):
		print("No-arg constructor")

demo1 = ConstrDemo();
# demo2 = ConstrDemo("Hello");
print("Main:", dir())
print("Class:", dir(ConstrDemo))

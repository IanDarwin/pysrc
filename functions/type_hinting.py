# Type-hinted variables have the type after the far name with a colon, like i:int
# They can be used in the function definition:

def foo(x:float) -> str:
	return str(x)

print(foo(123.45))

print(foo(123))

# But python does not enforce type checking (as usual for Python), unlike most langs.
print(foo("A string"))

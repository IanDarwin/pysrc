# Show that functions can be nested deeply, and
# that "nonlocal" will find the nearest enclosing,
# not tied to the immediate enclosing.

var = 0;

def outer():
	var = 42

	def middle():

		def inner():
			nonlocal var
			print("In inner, var =", var);
			var = 37
			print("In inner, var =", var);

		print("In middle, var =", var);
		inner()
		print("In middle, var =", var);

	print("In outer, var =", var);
	middle()
	print("In outer, var =", var);

print("Starting")

outer()

print("Done, var = ", var)

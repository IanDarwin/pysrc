# A 'class attribute' is like a static method in C-family (Java, C++, C#, etc)

# A class attribute and an instance variable of the same name are distinct!

# For class methods (which are subtly different from static methods), see
# https://www.geeksforgeeks.org/class-method-vs-static-method-python/

class One:
	name = "Kellogs"

o = One();
o.name = "Post"

print("o.name = " + o.name)
print("One.name = " + One.name)


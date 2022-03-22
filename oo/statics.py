# A class variable and an instance variable of the same name are distinct!

class One:
	name = "Kellogs"

o = One();
o.name = "Post"

print("o.name = " + o.name)
print("One.name = " + One.name)

# When pasting functions from one file to another, you must
# be careful to get the indentation right.

def fun1():
	print("In fun1")

	# "TODO: Cut this function from file 1 and paste it in file 2"
	def fun2():
		print("In fun2");

if __name__ == '__main__':
	fun1()
	fun2()

i = 0
s = 'Atlantic Ocean'

while True:
	n = s.find('an', i)
	if (n == -1):
		break;
	print(n)
	i = n + 1
	

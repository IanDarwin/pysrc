# It is not OK to modify the structure of a list while iterating it

def crashAndBurn():
	nums=list(range(5))
	for num in nums:
		print(num)
		nums.insert(0,'x')

if __name__ == '__main__':
	ans = input("Are you sure you want to loop forever?")
	if len(ans) > 0 and ans.lower()[0] == 'y':
		input("OK, it's your funeral. Hit <return> to start. Use CTRL/C to stop");
		crashAndBurn();

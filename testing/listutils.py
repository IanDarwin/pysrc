''' Simple list utilities. '''

def rotate(seq):
	''' rotate a list to the left by one position. '''
	return seq[1:] + [seq[0]]


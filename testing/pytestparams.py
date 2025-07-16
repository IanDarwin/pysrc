# parameterized tests

from pytest import mark

@mark.parametrize("one,two,expected",[
	(2,2,4),
	(3,4,7)
])
def testAdd(one,two,expected):
	assert one + two == expected

import unittest
import listutils

class MyTest(unittest.TestCase):
	def test(self):
		orig = [ 2, 4, 6 ]
		expected = [ 4, 6, 2 ]
		self.assertTrue(expected, listutils.rotate(orig))

if __name__ == '__main__':
        unittest.main()


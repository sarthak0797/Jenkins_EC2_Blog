import unittest

class Test(unittest.TestCase):

	def tests_(self):
		for i in range(1,5):
			s = i+i
			self.assertEqual(s,i+1)


if __name__ == '__main__':
    unittest.main()

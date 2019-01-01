import unittest

class Test(unittest.TestCase):

	def tests_(self):
		for i in range(1,5):
			s = i+i
			self.assertEqual(s,i+i)


if __name__ == '__main__':
    unittest.main()

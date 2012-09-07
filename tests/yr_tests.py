import unittest
from yr import yr

class yr_tests(unittest.TestCase):

	def create_yr_test(self):
		y = yr("Finland/Western_Finland/Turku")
		self.assertIsInstance(y, yr)
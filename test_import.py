import unittest

class InstallationTests(unittest.TestCase):

	def test_import_numpy(self):
		import numpy as np
		self.assertEqual(np.square(2), 4)

""" This is just to test the installation of numpy. The tests are commented out in the role tasks of
nansat and geospaas_core setup_python.yml files. To enable them you'll need to copy this file into the
shared folder.
"""
import unittest

class InstallationTests(unittest.TestCase):

	def test_import_numpy(self):
		import numpy as np
		self.assertEqual(np.square(2), 4)

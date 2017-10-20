"""
	Author: Luis_C-137
	(1) Create a unit test for 03_Float_Fix_Hex_Verilog.py

	Note: To run unittest use command: python -m unittest filename.py
"""

import unittest
import conversions as conv

class TestConversions(unittest.TestCase):

	def test_secondComplement(self):
		self.assertEqual(conv.secondComplement(15),"0000000F")
		self.assertEqual(conv.secondComplement(0),"00000000")
		self.assertEqual(conv.secondComplement(-15),"FFFFFFF1")

# This is used to compile as a normal python program
if __name__ == '__main__':
	unittest.main()
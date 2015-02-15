#!/usr/bin/python
# -*- encoding: utf-8 -*-

# docs https://docs.python.org/2/library/unittest.html#assert-methods
import unittest
from src.bank import Bank


"""
	Unittest class Bank
"""


class Test_bank(unittest.TestCase, Bank):

	def test_function_initial(self):
		self.assertIsNotNone(self.__init__)

	def test_createaccount(self):
		self.assertIsNone(self.CreateAccount(), '')

	def test_validatedata(self):
		self.assertEqual(self.ValidateData(), None)

	def test_queryaccount(self):
		self.assertNotEqual(self.QueryValueAccount('321123'), False)
		self.assertEqual(self.QueryValueAccount(), False)

unittest.main()
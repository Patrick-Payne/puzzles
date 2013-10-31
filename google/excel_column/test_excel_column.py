#!/usr/bin/env python3
'''
File: test_excel_column.py
Author: Patrick Payne
Date Created: Oct 30, 2013
Description: Tests the excel_column() routine in excel_column.py.
'''

import unittest
import pdb
from excel_column import get_column

class TestGetColumn(unittest.TestCase):
    """ Tests the excel_column() routine in excel_column.py. """

    def test_single_letter(self):
        """ Test case where the representation has only a single letter. """
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for number, letter in enumerate(letters):
            self.assertEqual(letter, get_column(number))

    def test_multiple_letter(self):
        """ Test cases where the representation has multiple letters. """
        self.assertEqual("AA", get_column(26))
        self.assertEqual("AB", get_column(27))
        self.assertEqual("AC", get_column(28))
        self.assertEqual("AZ", get_column(51))
        self.assertEqual("BA", get_column(52))
        self.assertEqual("BB", get_column(53))

if __name__ == '__main__':
    unittest.main()

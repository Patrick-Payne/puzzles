#!/usr/bin/env python3
'''
File: test_single_complete_cycle.py
Author: Patrick Payne
Date Created: Sep 24, 2013
Description: Tests the code in single_complete_cycle.py
'''

import unittest
from single_complete_cycle import is_complete_cycle

class TestSingleCompleteCycle(unittest.TestCase):
    """Test case for the is_complete_cycle() function. """

    def test_single_element(self):
        """Tests the case where we only have a single element."""
        self.assertTrue(is_complete_cycle([0]))
        self.assertTrue(is_complete_cycle([3]))
        self.assertTrue(is_complete_cycle([-3]))

    def test_true_cases(self):
        """Tests the multielement cases where True should be returned."""
        self.assertTrue(is_complete_cycle([1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_complete_cycle([-1, -1, -1, -1, -1, -1 , -1]))
        self.assertTrue(is_complete_cycle([1, 2, 2, -1]))
        self.assertTrue(is_complete_cycle([2, -1, 2, -2, 1, -2]))

    def test_false_cases(self):
        """Tests the multielement cases where False should be returned."""
        self.assertFalse(is_complete_cycle([2, 2, 2, 2, 2, 2]))
        self.assertFalse(is_complete_cycle([1, 2, 3, 4, 5, 6]))
        self.assertFalse(is_complete_cycle([0, 1, 1, 1, 1, 1]))
        self.assertFalse(is_complete_cycle([1, 1, 1, 1, 1, 0]))


if __name__ == "__main__":
    unittest.main()

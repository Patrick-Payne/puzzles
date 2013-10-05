#!/usr/bin/env python3
'''
File: test_get_missing_item.py
Author: Patrick Payne
Date Created: Oct 05, 2013
Description: Tests the missing_item function from get_missing_item.py.
'''
from get_missing_item import missing_item, NoMissingItemError
import unittest

class TestMissingItem(unittest.TestCase):
    """ A set of tests for the missing_item function. """

    def test_empty_lists(self):
        """ Tests the behaviour when one or both lists are empty. """
        # Test the cases where A is empty.
        with self.assertRaises(NoMissingItemError):
            missing_item([], [])

        with self.assertRaises(NoMissingItemError):
            missing_item([], [1, 2, 3])

        # Test the case where B is empty, but A has 1 element.
        self.assertEqual(missing_item([1], []), 1)
        self.assertEqual(missing_item([-12.5], []), -12.5)


    def test_equal_length_lists(self):
        """ Tests the behaviour when lists are equal in length. """
        # Test the case where B contains all the elements of A.
        with self.assertRaises(NoMissingItemError):
            missing_item([1], [1])

        with self.assertRaises(NoMissingItemError):
            missing_item([-1, 16, 2.2], [2.2, -1, 16])

        with self.assertRaises(NoMissingItemError):
            missing_item([2, 1010, 3201, 0.126, 5], [3201, 1010, 5, 2, 0.126])

        # Test the case where A contains an extra element.
        self.assertEqual(missing_item([1, 2, 3], [1, 2, 4]), 3)
        self.assertEqual(missing_item([5, -17, 0.5, 1], [0.5, 5, 1, 17]), -17)

    def test_a_is_longer(self):
        """ Tests the behaviour when list A is longer. """
        # Test the case where B contains all the elements of A.
        with self.assertRaises(NoMissingItemError):
            missing_item([1, 1], [1])

        with self.assertRaises(NoMissingItemError):
            missing_item([-1, 16, 16, 2.2], [2.2, -1, 16])

        with self.assertRaises(NoMissingItemError):
            missing_item([2, 1010, 3201, 5, 1010, 2], [3201, 1010, 5, 2])

        # Test the case where there are elements in A missing in B.
        self.assertEqual(missing_item([1, 2, 3], [1, 2]), 3)
        self.assertEqual(missing_item([5, -17, 0.5, 1], [0.5, 5, 1]), -17)

    def test_b_is_longer(self):
        """ Tests the behaviour when list B is longer. """
        # Test the case where B contains all the elements of A.
        with self.assertRaises(NoMissingItemError):
            missing_item([1], [1, 2, 3])

        with self.assertRaises(NoMissingItemError):
            missing_item([-1, 16, 2.2], [2.2, -1, 16, 42, 53])

        with self.assertRaises(NoMissingItemError):
            missing_item([2, 1010, 3201, 5], [3201, 1010, 5, 2, -1121, 20])

        # Test the case where there are elements in A missing in B.
        self.assertEqual(missing_item([1, 2, 3], [1, 2, 4, 5]), 3)
        self.assertEqual(missing_item([5, -17, 1, 10], [5, 1, 10, 11]), -17)


if __name__ == '__main__':
    unittest.main(verbosity=3)

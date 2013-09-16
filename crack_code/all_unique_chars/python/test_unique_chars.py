#!/usr/bin/env python3
'''
File: test_unique_chars.py
Author: Patrick Payne
Date Created: Sep 15, 2013
Description: Unit tests for the functions in unique_chars.py
'''
import unittest
import string
from unique_chars import all_unique_chars, all_unique_chars_no_set


class TestAllUniqueChars(unittest.TestCase):
    """ Test the all_unique_chars() function."""

    def test_empty_string(self):
        """ Test the case where the string is empty. """
        self.assertTrue(all_unique_chars(""))

    def test_single_char(self):
        """ Test the case where the string has only 1 character. """
        self.assertTrue(all_unique_chars("a"))
        self.assertTrue(all_unique_chars("b"))

    def test_multiple_char_not_unique(self):
        """ Test the case where we have multiple characters, not all unique."""
        self.assertFalse(all_unique_chars("aa"))
        self.assertFalse(all_unique_chars("alabama"))
        self.assertFalse(all_unique_chars("Ricardio"))
        self.assertFalse(all_unique_chars("aardvark"))
        self.assertFalse(all_unique_chars("Zimbabwe"))
        self.assertFalse(all_unique_chars("....What?...."))

    def test_multiple_char_unique(self):
        """ Test the case where we have multiple characters, all unique."""
        self.assertTrue(all_unique_chars("ab"))
        self.assertTrue(all_unique_chars("ba"))
        self.assertTrue(all_unique_chars("make"))
        self.assertTrue(all_unique_chars("thorn"))
        self.assertTrue(all_unique_chars("malibu"))
        self.assertTrue(all_unique_chars(string.ascii_letters))


class TestAllUniqueCharsNoSet(unittest.TestCase):
    """ Test the all_unique_chars() function."""

    def test_empty_string(self):
        """ Test the case where the string is empty. """
        self.assertTrue(all_unique_chars_no_set(""))

    def test_single_char(self):
        """ Test the case where the string has only 1 character. """
        self.assertTrue(all_unique_chars_no_set("a"))
        self.assertTrue(all_unique_chars_no_set("b"))

    def test_multiple_char_not_unique(self):
        """ Test the case where we have multiple characters, not all unique."""
        self.assertFalse(all_unique_chars_no_set("aa"))
        self.assertFalse(all_unique_chars_no_set("alabama"))
        self.assertFalse(all_unique_chars_no_set("Ricardio"))
        self.assertFalse(all_unique_chars_no_set("aardvark"))
        self.assertFalse(all_unique_chars_no_set("Zimbabwe"))
        self.assertFalse(all_unique_chars_no_set("....What?...."))

    def test_multiple_char_unique(self):
        """ Test the case where we have multiple characters, all unique."""
        self.assertTrue(all_unique_chars_no_set("ab"))
        self.assertTrue(all_unique_chars_no_set("ba"))
        self.assertTrue(all_unique_chars_no_set("make"))
        self.assertTrue(all_unique_chars_no_set("thorn"))
        self.assertTrue(all_unique_chars_no_set("malibu"))
        self.assertTrue(all_unique_chars_no_set(string.ascii_letters))


if __name__ == '__main__':
    unittest.main()

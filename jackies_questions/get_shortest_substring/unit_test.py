#!/usr/bin/env python3
'''
File: unit_test.py
Author: Patrick Payne
Description: Unit testing for get_shortest_substring.py.
'''
import substring
import unittest
import pdb


class TestGetIndices(unittest.TestCase):
    """ TestCase for substring.get_indices()"""
    def test_empty_input(self):
        """ Test cases where there are empty inputs. """
        # Both the search string and the collection of letters are empty.
        indices, indices_by_letter = substring.get_indices('', "")
        self.assertEqual(indices, [])
        self.assertEqual(indices_by_letter, {})

        # The string is nonempty, but there are still no letters
        indices, indices_by_letter = substring.get_indices('', "Foo.")
        self.assertEqual(indices, [])
        self.assertEqual(indices_by_letter, {})

        # There are letters, but the searched string is empty
        indices, indices_by_letter = substring.get_indices('abc', '')
        self.assertEqual(indices, [])
        self.assertEqual(indices_by_letter, {'a': [], 'b': [], 'c': []})

    def test_single_letter(self):
        """ Test cases where we are only looking for a single letter."""
        # The letter is not present in the string.
        indices, indices_by_letter = substring.get_indices('a', "bbbb")
        self.assertEqual(indices, [])
        self.assertEqual(indices_by_letter, {'a': []})

        # The letter is present at the zero index.
        indices, indices_by_letter = substring.get_indices('z', "zbbb")
        self.assertEqual(indices, [0])
        self.assertEqual(indices_by_letter, {'z': [0]})

        # The letter is present at a nonzero index.
        indices, indices_by_letter = substring.get_indices('y', "bybb")
        self.assertEqual(indices, [1])
        self.assertEqual(indices_by_letter, {'y': [1]})

        indices, indices_by_letter = substring.get_indices('a', "bbab")
        self.assertEqual(indices, [2])
        self.assertEqual(indices_by_letter, {'a': [2]})

        # The letter is present in multiple consecutive locations.
        indices, indices_by_letter = substring.get_indices('a', "aab")
        self.assertEqual(indices, [0, 1])
        self.assertEqual(indices_by_letter, {'a': [0, 1]})

        # The letter is present in multiple nonconsecutive locations.
        indices, indices_by_letter = substring.get_indices('a', "claptrap")
        self.assertEqual(indices, [2, 6])
        self.assertEqual(indices_by_letter, {'a': [2, 6]})

    def test_two_letters(self):
        """ Test cases where we are searching for 2 letters. """
        # The letters are both not present in the string.
        search_string = "sdfghkl;"
        indices, indices_by_letter = substring.get_indices("ab", search_string)
        self.assertEqual(indices, [])
        self.assertEqual(indices_by_letter, {'a': [], 'b': []})

        # One of the two letters is in the string.
        search_string = "youtube"
        indices, indices_by_letter = substring.get_indices("ab", search_string)
        self.assertEqual(indices, [5])
        self.assertEqual(indices_by_letter, {'a': [], 'b': [5]})

        # Both letters are in the string.
        search_string = "zaboomafoo"
        indices, indices_by_letter = substring.get_indices("ab", search_string)
        self.assertEqual(indices, [1, 2, 6])
        self.assertEqual(indices_by_letter, {'a': [1, 6], 'b': [2]})

        search_string = "ababab"
        indices, indices_by_letter = substring.get_indices("ab", search_string)
        expected_indices = list(range(len(search_string)))
        self.assertEqual(indices, expected_indices)
        self.assertEqual(indices_by_letter, {'a': [0, 2, 4], 'b': [1, 3, 5]})

    def test_multiple_letters(self):
        """ Test cases where we are searching for multiple letters. """
        # None of the letters are present.
        search_str = "efghijk"
        indices, indices_by_letter = substring.get_indices("abc", search_str)
        self.assertEqual(indices, [])
        self.assertEqual(indices_by_letter, {'a': [], 'b': [], 'c': []})

        # One of the letters is present.
        search_str = "cfghijk"
        indices, indices_by_letter = substring.get_indices("abc", search_str)
        self.assertEqual(indices, [0])
        self.assertEqual(indices_by_letter, {'a': [], 'b': [], 'c': [0]})

        search_str = "0123bb...!#@!"
        indices, indices_by_letter = substring.get_indices("abc", search_str)
        self.assertEqual(indices, [4, 5])
        self.assertEqual(indices_by_letter, {'a': [], 'b': [4, 5], 'c': []})

        # All of the letters are present once.
        search_str = "abc"
        indices, indices_by_letter = substring.get_indices("abc", search_str)
        self.assertEqual(indices, [0, 1, 2])
        self.assertEqual(indices_by_letter, {'a': [0], 'b': [1], 'c': [2]})

        search_str = "0123abc"
        indices, indices_by_letter = substring.get_indices("abc", search_str)
        self.assertEqual(indices, [4, 5, 6])
        self.assertEqual(indices_by_letter, {'a': [4], 'b': [5], 'c': [6]})

        # All of the letters are present multiple times.
        search_str = "abc" * 10
        indices, indices_by_letter = substring.get_indices("abc", search_str)
        expected_indices = list(range(len(search_str)))
        expected_a_indices = list(range(0, len(search_str), 3))
        expected_b_indices = list(range(1, len(search_str), 3))
        expected_c_indices = list(range(2, len(search_str), 3))
        self.assertEqual(indices, expected_indices)
        self.assertEqual(indices_by_letter,
                         {'a': expected_a_indices,
                          'b': expected_b_indices,
                          'c': expected_c_indices})


class TestGetMaxStartingIndex(unittest.TestCase):
    """ Tests the substring.max_starting_index() function. """
    def test_invalid_inputs(self):
        """ Test the case where there are no possible starting indices. """
        # A single letter with no indices.
        indices_by_letter = {'a': []}
        with self.assertRaises(substring.NoSubstringFound):
            substring.max_starting_index(indices_by_letter)

        # Multiple letters with no indices.
        indices_by_letter = {'a': [], 'b': []}
        with self.assertRaises(substring.NoSubstringFound):
            substring.max_starting_index(indices_by_letter)

        # Multiple letters, but not all have indices.
        indices_by_letter = {'a': [], 'b': [1]}
        with self.assertRaises(substring.NoSubstringFound):
            substring.max_starting_index(indices_by_letter)

        indices_by_letter = {'a': [10], 'b': [], 'c': [3]}
        with self.assertRaises(substring.NoSubstringFound):
            substring.max_starting_index(indices_by_letter)

    def test_single_letter(self):
        """ Test the case where we are looking for only a single letter. """
        # The maximum starting index will be the largest index of that letter.
        indices_by_letter = {'a': [0]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 0)

        indices_by_letter = {'a': [0, 1]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 1)

        indices_by_letter = {'a': [0, 1, 2, 9]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 9)

    def test_two_letters(self):
        """ Test the case where we are looking for two letters. """
        # There is only one possible substring.
        indices_by_letter = {'a': [0], 'b': [1]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 0)

        indices_by_letter = {'a': [1], 'b': [2]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 1)

        # There are multiple possible substrings.
        indices_by_letter = {'a': [1, 3], 'b': [2]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 2)

        indices_by_letter = {'a': [1, 3, 5], 'b': [2]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 2)

        indices_by_letter = {'a': [3, 5, 9], 'b': [2, 6, 7]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 7)

    def test_multiple_letters(self):
        """ Test the case where we are looking for multiple letters. """
        # There is only one possible substring.
        indices_by_letter = {'a': [0], 'b': [1], 'c': [2]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 0)

        indices_by_letter = {'a': [1], 'b': [2], 'c': [3]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 1)

        # There are multiple possible substrings.
        indices_by_letter = {'a': [0, 3], 'b': [1], 'c': [2]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 1)

        indices_by_letter = {'a': [0, 3], 'b': [5], 'c': [2, 7]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 3)

        indices_by_letter = {'a': [0, 3, 6], 'b': [1, 4, 7], 'c': [2, 5, 8]}
        self.assertEqual(substring.max_starting_index(indices_by_letter), 6)


class TestNextIndex(unittest.TestCase):
    """ Tests the substring.next_index() function. """
    def test_regular_case(self):
        """ Test the regular use case for the function. """
        next_index = substring.next_index(0, [0, 1])
        self.assertEqual(next_index, 1)

        next_index = substring.next_index(0, [0, 3])
        self.assertEqual(next_index, 3)

        next_index = substring.next_index(3, [0, 3, 7, 9])
        self.assertEqual(next_index, 7)

        next_index = substring.next_index(7, [0, 3, 7, 9])
        self.assertEqual(next_index, 9)

        next_index = substring.next_index(1, [0, 3, 7, 9])
        self.assertEqual(next_index, 3)


class TestGetShortestSubstring(unittest.TestCase):
    """ Tests the substring.get_shortest_substring() function. """
    def test_no_substring_found(self):
        """ Test the case where there are no valid substrings. """
        with self.assertRaises(substring.NoSubstringFound):
            substring.get_shortest_substring("a", "")

        with self.assertRaises(substring.NoSubstringFound):
            substring.get_shortest_substring("a", "Cote D'Ivoire")

        with self.assertRaises(substring.NoSubstringFound):
            substring.get_shortest_substring("banz", "banana")

    def test_no_letter(self):
        """ Test the case where no letters are provided. """
        self.assertEqual(substring.get_shortest_substring('', "banana"), '')
        self.assertEqual(substring.get_shortest_substring('', "Troika"), '')

    def test_single_letter(self):
        """ Test the case where we are searching for only a single letter."""
        # The letter is at the beginning of the string.
        self.assertEqual(substring.get_shortest_substring('a', "a"), 'a')
        self.assertEqual(substring.get_shortest_substring('d', "do"), 'd')
        self.assertEqual(substring.get_shortest_substring('c', "cab"), 'c')
        self.assertEqual(substring.get_shortest_substring('b', "bide"), 'b')

        # The letter is at the end of the string.
        self.assertEqual(substring.get_shortest_substring('o', "so"), 'o')
        self.assertEqual(substring.get_shortest_substring('d', "ballad"), 'd')
        self.assertEqual(substring.get_shortest_substring('f', "aloof"), 'f')
        self.assertEqual(substring.get_shortest_substring('e', "durable"), 'e')

        # The letter is exactly in the middle of the string.
        self.assertEqual(substring.get_shortest_substring('o', "sos"), 'o')
        self.assertEqual(substring.get_shortest_substring('b', "fubar"), 'b')

        # The letter is in various locations.
        self.assertEqual(substring.get_shortest_substring('d', "grande"), 'd')
        self.assertEqual(substring.get_shortest_substring('e', "Kreyzig"), 'e')

        # The letter is present multiple times.
        self.assertEqual(substring.get_shortest_substring('z', "zzzzzz"), 'z')
        self.assertEqual(substring.get_shortest_substring('p', "apple"), 'p')

    def test_two_letters(self):
        """
        Test the case where we are looking for substrings containing two
        different letters.
        """
        # The two searched letters are immediately adjacent.
        result = substring.get_shortest_substring('ab', "absolutely right.")
        self.assertEqual(result, "ab")

        # pdb.set_trace() 
        result = substring.get_shortest_substring('gr', "programming")
        self.assertEqual(result, "gr")

        result = substring.get_shortest_substring('ng', "canoeing")
        self.assertEqual(result, "ng")

        # The two searched letters are seperated by a single character.
        result = substring.get_shortest_substring('bd', "bad")
        self.assertEqual(result, "bad")

        result = substring.get_shortest_substring('nm', "animal")
        self.assertEqual(result, "nim")

        result = substring.get_shortest_substring('lr', "regular")
        self.assertEqual(result, "lar")

        # The two searched letters are seperated by multiple characters.
        result = substring.get_shortest_substring('rd', "read")
        self.assertEqual(result, "read")

        result = substring.get_shortest_substring('bm', "zaboomafoo")
        self.assertEqual(result, "boom")

        result = substring.get_shortest_substring('pb', "possible")
        self.assertEqual(result, "possib")

        # One of the letters appears multiple times.
        result = substring.get_shortest_substring('ab', "a...ba")
        self.assertEqual(result, "ba")

        result = substring.get_shortest_substring('ba', "ab...a")
        self.assertEqual(result, "ab")

        result = substring.get_shortest_substring('fu', "fuuuuuuuuuu")
        self.assertEqual(result, "fu")

        result = substring.get_shortest_substring('df', "d..f.d")
        self.assertEqual(result, "f.d")

        # Both of the letters appear multiple times.
        result = substring.get_shortest_substring('df', "df.df.df.df.df.")
        self.assertEqual(result, "df")

        result = substring.get_shortest_substring('ab', "abra kadabra")
        self.assertEqual(result, "ab")

        result = substring.get_shortest_substring('db', "bad. baad. baaad.")
        self.assertEqual(result, "bad")

    def test_multiple_letters(self):
        """
        Test the case where we are looking for substrings containing more than
        two different letters.
        """
        # Each letter appears only once.
        result = substring.get_shortest_substring('elt', "late")
        self.assertEqual(result, "late")

        result = substring.get_shortest_substring('bri', "rabies")
        self.assertEqual(result, "rabi")

        # There are two possible substrings.
        result = substring.get_shortest_substring('pkd', "porkedup")
        self.assertEqual(result, "kedup")

        result = substring.get_shortest_substring('tin', "munitions")
        self.assertEqual(result, "nit")

        result = substring.get_shortest_substring('abm', "lamb balm")
        self.assertEqual(result, "amb")

        # There are many possible substrings.
        result = substring.get_shortest_substring('ab', "a.b  a..b  a....b")
        self.assertEqual(result, "a.b")

        result = substring.get_shortest_substring('yut', "Turkyturnkeyturk")
        self.assertEqual(result, "ytu")

        result = substring.get_shortest_substring('abc', "a..c...b.a..c..b")
        self.assertEqual(result, "b.a..c")


if __name__ == '__main__':
    unittest.main(verbosity=3)

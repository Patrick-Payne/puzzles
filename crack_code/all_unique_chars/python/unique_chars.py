#!/usr/bin/env python3
'''
File: unique_chars.py
Author: Patrick Payne
Date Created: Sep 15, 2013
Description: Implements a simple function to check if all of the characters
    in a python string are unique.
'''

def all_unique_chars(string):
    """ Tests if a string only contains unique characters."""
    unique_chars = set()
    for char in string:
        if char in unique_chars:
            # We saw the character before, so it is not unique.
            return False
        else:
            unique_chars.add(char)

    # If we get here, all of the characters were unique.
    return True

def all_unique_chars_no_set(string):
    """
    Tests if a string only contains unique characters without using any other
    data structures.
    """
    for index in range(len(string) - 1):
        # Check the rest of the string for this character.
        if string[index] in string[index + 1:]:
            return False

    # If we get this far, none of the characters were repeated in the string.
    return True

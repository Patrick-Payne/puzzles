"""
File: excel_column.py
Author: Patrick Payne
Date Created: Oct 30, 2013
Description: From a positive integer, determine its form as an excel column.
"""


def get_column(input_number):
    """
    Given a positive integer, return a string representing the excel column
    label it would be given, e.g. 0 -> “A”, 1 -> “B”, 26 -> AA, and so on.
    """
    assert input_number >= 0, "Number must be positive."
    
    # letters is a list whose values represent the letter form of the index.
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Get the lowest order letter.
    number = input_number
    output_string = letters[number % 26]
    number //= 26

    while (number > 0):
        # Determine the lowest order letter.
        output_string = letters[(number % 26) - 1] + output_string

        # Move on the next letter in the excel column name.
        number //= 26

    return output_string

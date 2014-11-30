#!/usr/bin/env python3
"""
File: telephone_number_words.py
Author: Patrick Payne
Date Created: Nov 30, 2014
Description: Given a seven digit phone number, print out all possible
    combinations of words it can represent.
"""
import sys

LETTER_FROM_DIGIT = {"0": [" "], "1": [""], "2": ["a", "b", "c"],
                     "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                     "5": ["j", "k", "l"], "6": ["m", "n", "o"],
                     "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"],
                     "9": ["w", "x", "y", "z"]}


def recursive_print_telephone_word(digits_remaining, word_so_far):
    """Recursively construct all possible words made up of of the suffix
    word_so_far and the list of telephone digits digits_remaining.
    """
    if len(digits_remaining) == 0:
        print(word_so_far)

    else:
        new_digits_remaining = digits_remaining[:]
        digit = new_digits_remaining.pop()
        for letter in LETTER_FROM_DIGIT[digit]:
            new_word_so_far = letter + word_so_far
            recursive_print_telephone_word(new_digits_remaining,
                                           new_word_so_far)


def print_telephone_word(number):
    digits = list(str(number))
    recursive_print_telephone_word(digits, "")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} {{telephone number}}".format(sys.argv[0]))
        sys.exit(-1)

    try:
        number = int(sys.argv[1])
    except:
        print("Invalid telephone number: {}".format(sys.argv[1]))
        sys.exit(-1)

    print_telephone_word(number)
    sys.exit(0)

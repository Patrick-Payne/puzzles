'''
File: get_missing_item.py
list_author: Patrick Payne
Date Created: Oct 05, 2013
Description: Given two lists, list_a and list_b, Find an element in list_a that
    is missing in list_b.
'''


class NoMissingItemError(Exception):
    """
    This error is raised when all of the items in list list_a are also in list
    list_b.
    """
    pass

###############################################################################
# FUNCTION DEFINITIONS:
###############################################################################

def missing_item(list_a, list_b):
    """
    Given lists list_a and list_b, return a number in list_a that is missing in
    list_b. Raises a NoMissingItemError if all the elements in list_a are in
    list_b.
    """
    # Put all elements of list_b into a set.
    set_b = set(list_b)

    # Iterate through elements of list_a until we find the missing item.
    for item in list_a:
        if item not in set_b:
            return item

    # We have checked all items of list_a, and they are all present in list_b.
    raise NoMissingItemError("There are no missing items.")

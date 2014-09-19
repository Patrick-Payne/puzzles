#!/usr/bin/env python3

import unittest

def swap(numbers, index1, index2):
    """Swap the items at index1 and index2 in list numbers."""
    temp = numbers[index1]
    numbers[index1] = numbers[index2]
    numbers[index2] = temp

def put_boxes_in_order(start_list):
    """Given a start_list with numbers 1...n in any order, put them in order.
    Preconditions:
        len(start_list) == n + 1
        start_list only contains the integer numbers 1 to n, as well as the vacancy represented by None, with no duplicates.
    Returns: A new list, with the numbers in order from 1 to n, with the vacancy at the end.
    """ 
    
    new_list = start_list[:]
    # keep the index at the end of the list.
    vacancy_index = new_list.index(None)
    swap(new_list, vacancy_index, len(new_list) - 1)
    vacancy_index = len(new_list) - 1

    for index in range(len(new_list) - 1):
        value = new_list[index]
        # See if the object is in the right position. if so, increment
        if value == index + 1:
            continue

        # If not, move the object occupying the correct location to the
        # vacancy, and move the current object to its proper location.
        swap(new_list, value - 1, vacancy_index)
        swap(new_list, index, value - 1)
        swap(new_list, index, vacancy_index)

    return new_list

class TestPutBoxesInOrder(unittest.TestCase):
    """Provides basic unit testing for the box ordering function. """
    def test_empty_list(self):
        """Tests the case where the input list is empty."""
        self.assertEqual([None], put_boxes_in_order([None]))
    
    def test_singleton_list(self):
        """Tests case where list has only one element."""
        self.assertEqual([1, None], put_boxes_in_order([1, None]))
        self.assertEqual([1, None], put_boxes_in_order([None, 1]))

    def test_doubleton_list(self):
        """Tests case where list has two elements."""
        self.assertEqual([1, 2, None], put_boxes_in_order([1, 2, None]))
        self.assertEqual([1, 2, None], put_boxes_in_order([None, 1, 2]))
        self.assertEqual([1, 2, None], put_boxes_in_order([1, None, 2]))
        self.assertEqual([1, 2, None], put_boxes_in_order([2, 1, None]))
        self.assertEqual([1, 2, None], put_boxes_in_order([None, 2, 1]))

    def test_large_list(self):
        """Tests the case where we have many elements in the list. """
        start_list = [7, 6, 5, 4, 3, 2, 1, None]
        target_list = [1, 2, 3, 4, 5, 6, 7, None]
        self.assertEqual(target_list, put_boxes_in_order(start_list))
        self.assertEqual(target_list, put_boxes_in_order(target_list))
    

if __name__ == "__main__":
    unittest.main()

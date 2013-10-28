#!/usr/bin/env python3
"""
File: test_line_through_most_points.py
Author: Patrick Payne
Date Created: Oct 27, 2013
Description: Tests line_through_most_points.py. Look there for documentation.
"""

import pdb
import unittest
from line_through_most_points import find_line

class BasicTestFindLine(unittest.TestCase):
    """ Tests the find_line() function from line_through_most_points.py. """

    def test_no_line(self):
        """ Tests find_line() when the list is empty, or a singleton. """
        self.assertEqual(None, find_line([]))
        self.assertEqual(None, find_line([(1, 1)]))

    def test_single_line_segment(self):
        """ Test the case where there is only 1 line segment possible. """
        # Test very basic case.
        points = [(0, 0), (1, 1)]
        slope, point = find_line(points)
        self.assertEqual(slope, 1.0)
        self.assertIn(point, points)

        # Make result is the same if we reverse the order of points.
        points = [(1, 1), (0, 0)]
        slope, point = find_line(points)
        self.assertEqual(slope, 1.0)
        self.assertIn(point, points)

        # Test a case with negative slope.
        points = [(0, 0), (1, -1)]
        slope, point = find_line(points)
        self.assertEqual(slope, -1.0)
        self.assertIn(point, points)

        # Test a case where we have a horizontal line.
        points = [(0, 0), (1, 0)]
        slope, point = find_line(points)
        self.assertEqual(slope, 0.0)
        self.assertIn(point, points)

        # Now test a case where we have a vertical line.
        points = [(0, 0), (0, 1)]
        slope, point = find_line(points)
        self.assertEqual(slope, None)
        self.assertIn(point, points)

    def test_multiple_line_segments(self):
        """ Tests cases where we have multiple possible line segments."""
        # 3 colinear points, 1 outlier
        points = [(0, 0), (1, 1), (-1, -1), (10, 2)]
        slope, point = find_line(points)
        self.assertEqual(slope, 1.0)
        self.assertIn(point, [(0, 0), (1, 1), (-1, -1)])

        points = [(0, 0), (0, 1), (0, -1), (1, 1)]
        slope, point = find_line(points)
        self.assertEqual(slope, None)
        self.assertIn(point, [(0, 0), (0, 1), (0, -1)])

        # 1 line has 4 colinear points, the others have 3 or less.
        points = [(0, 0), (1, 1), (-1, -1), (1, -1), (-1, 1), (2, 2)]
        slope, point = find_line(points)
        self.assertEqual(slope, 1.0)
        self.assertIn(point, [(0, 0), (1, 1), (-1, -1), (2, 2)])


if __name__ == '__main__':
    unittest.main()

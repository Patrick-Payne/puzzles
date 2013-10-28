"""
File: line_through_most_points.py
Author: Patrick Payne
Date Created: Oct 27, 2013
Description: Given a set of points, determine an equation of the line that
    passes through the largest number of lines. This implementation uses
    O(n^2) time and O(n) space.
"""


def find_line(points):
    """
    Returns the equation of a line that passes through the most
    points in `points`. `points` is a list containing 2-tuples
    representing the (x,y) coordinates of a point, and the result is
    a 2 tuple containing the slope and a point. If the line is vertical,
    its value is represented by None. If the list is empty or only has one
    element, return None.
    """

    # Handle the empty and singleton edge cases.
    if (len(points) < 2):
        return None

    # Track the length and formula of the longest line so far.
    most_points = 0
    most_slope = 0.0
    most_point = (0, 0)

    # For each point, find line through that point that goes through the
    # the largest number of other points.
    for index, start_point in enumerate(points):
        # Create a dictionary, where the keys are slopes, and the values
        # are the number of points sharing that slope.
        slopes = {}
        for point in points[index + 1:]:
            if (point[0] == start_point[0]):
                slope = None
            else:
                slope = (point[1] - start_point[1])/(point[0] - start_point[0])
            slopes[slope] = slopes.get(slope, 0) + 1

        # Determine which slope corresponds to the most points.
        most_through_start_point = 0
        best_slope_through_start_point = 0
        for slope in slopes:
            if slopes[slope] > most_through_start_point:
                most_through_start_point = slopes[slope]
                best_slope_through_start_point = slope

        # See if the line through this point is the best line so far.
        if most_through_start_point > most_points:
            most_points = most_through_start_point
            most_slope = best_slope_through_start_point
            most_point = start_point

    # We are out of the main loop; simply return the result.
    return (most_slope, most_point)

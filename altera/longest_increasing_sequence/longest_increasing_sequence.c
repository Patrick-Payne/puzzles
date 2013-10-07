/******************************************************************************
 * File: longest_increasing_sequence.h
 * Author: Patrick Payne
 * Date Created: Oct 07, 2013
 * Purpose: Defines the LongestIncreasingSequence function, which returns the
 *   length of the longest increasing sequence of integers in an array.
 * Copyright 2013 by Patrick Payne.
 *****************************************************************************/

#include "longest_increasing_sequence.h"

/******************************************************************************
 * PUBLIC FUNCTION DECLARATIONS:
 *****************************************************************************/ 

/*! @brief given an array of integers, returns the length of the longest
 *      (strictly) increasing sequence in the array.
 *  @param list The array of integers in question.
 *  @param length The length of the valid portion of the array.
 *  @return The length of the longest increasing sequence in list.
 */
int LongestIncreasingSequence(int *list, int length) {
  int longest_streak = 1;
  int current_streak = 1;

  // Handle the edge case where length is zero.
  if (length == 0) {
    return 0;
  }

  for (int i = 1; i < length; i++) {
    if (list[i] > list[i-1]) {
      current_streak++;
    } else {
      if (longest_streak < current_streak) {
        longest_streak = current_streak;
      }
      current_streak = 1;
    }
  } /* for */

  // Handle the edge case where the longest streak is at the end of the list.
  if (longest_streak < current_streak) {
    longest_streak = current_streak;
  }

  return longest_streak;
}

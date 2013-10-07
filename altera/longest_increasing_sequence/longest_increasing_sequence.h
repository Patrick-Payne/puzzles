/******************************************************************************
 * File: longest_increasing_sequence.h
 * Author: Patrick Payne
 * Date Created: Oct 07, 2013
 * Purpose: Declares the LongestIncreasingSequence function, which returns the
 *   length of the longest increasing sequence of integers in an array.
 * Copyright 2013 by Patrick Payne.
 *****************************************************************************/

/******************************************************************************
 * PUBLIC FUNCTION DECLARATIONS:
 *****************************************************************************/ 

/*! @brief given an array of integers, returns the length of the longest
 *      (strictly) increasing sequence in the array.
 *  @param list The array of integers in question.
 *  @param length The length of the valid portion of the array.
 *  @return The length of the longest increasing sequence in list.
 */
int LongestIncreasingSequence(int *list, int length);

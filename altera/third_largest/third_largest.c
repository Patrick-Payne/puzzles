/******************************************************************************
 * File: third_largest.c
 * Author: Patrick Payne
 * Date Created: Oct 10, 2013
 * Purpose: Implements the third_largest() function, which returns the third
 *     largest item in an array.
 * Copyright 2013 by Patrick Payne.
 *****************************************************************************/

#include <assert.h>
#include "third_largest.h"


/*! @brief Finds the third largest element in an array, and returns it.
 *  @param list The list to search through, of size greater or equal to three.
 *  @param size The size of the list.
 *  @return The third largest item in the array.
 */
int third_largest(int *list, int size) {
  assert(size >= 3);

  // Initially, all of the top three values are the first item in the list.
  int first = list[0];
  int second = list[0];
  int third = list[0];

  for (int i = 0; i < size; i++) {
    if (list[i] > first) {
      third = second;
      second = first;
      first = list[i];
    } else if (list[i] > second) {
      third = second;
      second = list[i];
    } else if (list[i] > third) {
      third = list[i];
    }
  }

  return third;
}

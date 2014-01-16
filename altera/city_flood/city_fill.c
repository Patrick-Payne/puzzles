/******************************************************************************
 * File: city_fill.c
 * Author: Patrick Payne
 * Date Created: Oct 14, 2013
 * Purpose: Defines the functions declared in city_fill.h.
 * Copyright 2013 by Patrick Payne.
 *****************************************************************************/

#include "city_fill.h"

/******************************************************************************
 * MACRO DEFINITIONS:
 *****************************************************************************/ 
#define MIN(x, y) (((x) <= (y)) ? (x) : (y))

/******************************************************************************
 * PUBLIC FUNCTION DEFINITIONS:
 *****************************************************************************/ 

/*! @brief Calculates the total volume of floodwater that would accumulate in
 *      the passed in city. See file header for details.
 *  @param list The city, represented as an array.
 *  @param size The number of slots the city occupies.
 *  @return The number of units of floodwater accumulated.
 */
int FloodVolume(int *list, int size) {
  int total_volume = 0;

  // Get the indices that mark the first basin water will accumulate in.
  int left_index = GetNextStartIndex(list, size, 0);
  int right_index = GetNextEndIndex(list, size, left_index);

  while ((left_index != INVALID_INDEX) && (right_index != INVALID_INDEX)) {
    // The basin will fill with water up to the height of the shorter of the
    // two endpoints of the basin.
    int fill_height = MIN(list[left_index], list[right_index]);

    // Find the volume of the current basin.
    int current_volume = 0;
    for (int i = left_index + 1; i < right_index; i++) {
      if (list[i] < fill_height) {
        current_volume += fill_height - list[i];
      }
    }
    total_volume += current_volume;

    // Go to the next basin, if one exists.
    left_index = GetNextStartIndex(list, size, right_index);
    right_index = GetNextEndIndex(list, size, left_index);
  }

  return total_volume;
}


/*! @brief Determines the starting end of the next water accumulation region
 *     of the city, i.e. the leftmost edge of a basin.
 *  @param list The city, represented as an array.
 *  @param size The number of slots the city occupies.
 *  @param start The index to start the search at.
 *  @return The index of the next starting edge, INVALID_INDEX if none exist.
 */
int GetNextStartIndex(int *list, int size, int start) {
  // If an invalid index is set for start, just return INVALID_INDEX.
  if (start == INVALID_INDEX) {
    return INVALID_INDEX;
  }

  int index = start;
  while ((index < size) && (list[index] <= list[index + 1])) {
    index++;
  }

  // We cannot start a basin on the right edge of the city.
  if (index >= size - 1) {
    return INVALID_INDEX;
  } else {
    return index;
  }
}


/*! @brief Determines the end of the current water accumulation region
 *     of the city, i.e. the rightmost edge of a basin.
 *  @param list The city, represented as an array.
 *  @param size The number of slots the city occupies.
 *  @param start The index to start the search at.
 *  @return The index of the ending edge, INVALID_INDEX if none exist.
 */
int GetNextEndIndex(int *list, int size, int start) {
  if (start == INVALID_INDEX) {
    return INVALID_INDEX;
  }
  int index = start + 1;

  while (index < size - 1) {
    if ((list[index] > list[index - 1]) && (list[index] >= list[index + 1])) {
      // Rule out the possibility that this is just a temporary plateau.
      while ((index < size - 1) && (list[index] == list[index + 1])) {
        index++;
      }
      if (list[index] > list[index + 1]) {
      return index;
      }
    } else {
      index++;
    }
  }

  // Check the edge case where we hit the last index without finding an end.
  if ((index < size) && (list[index] > list[index - 1])) {
    return index;
  } else {
    return INVALID_INDEX;
  }
}

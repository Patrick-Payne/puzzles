/******************************************************************************
 * File: city_fill.c
 * Author: Patrick Payne
 * Date Created: Oct 14, 2013
 * Purpose: Defines the functions declared in city_fill.h.
 * Copyright 2013 by Patrick Payne.
 *****************************************************************************/

#include "city_fill.h"

/******************************************************************************
 * PUBLIC FUNCTION DEFINITIONS:
 *****************************************************************************/ 

/*! @brief Calculates the total volume of floodwater that would accumulate in
 *      the passed in city. See file header for details.
 *  @param list The city, represented as an array.
 *  @param size The number of slots the city occupies.
 *  @return The number of units of floodwater accumulated.
 */
int FloodVolume (int *list, int size) {
  return 1;
}


/*! @brief Determines the starting end of the next water accumulation region
 *     of the city, i.e. the leftmost edge of a basin.
 *  @param list The city, represented as an array.
 *  @param size The number of slots the city occupies.
 *  @param start The index to start the search at.
 *  @return The index of the next starting edge, INVALID_INDEX if none exist.
 */
int GetNextStartIndex(int *list, int size, int start) {
  return 1;
}


/*! @brief Determines the end of the current water accumulation region
 *     of the city, i.e. the rightmost edge of a basin.
 *  @param list The city, represented as an array.
 *  @param size The number of slots the city occupies.
 *  @param start The index to start the search at.
 *  @return The index of the ending edge, INVALID_INDEX if none exist.
 */
int GetNextEndIndex(int *list, int size, int start) {
  return 1;
}

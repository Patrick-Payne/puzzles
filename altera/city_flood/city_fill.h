/******************************************************************************
 * File: city_fill.c
 * Author: Patrick Payne
 * Date Created: Oct 14, 2013
 * Purpose: Declares the FloodVolume() routine, which determines the volume of
 *  rainwater that would collect in a 2D city. The city is represented by an
 *  array of integers representing the height of the building on that index.
 *  e.g.  [1, 2, 4, 1, 4, 2, 1]
 *              ###   ###                 ###***###   
 *              ###   ###       =>        ###***###
 *           ######   ######           ######***######
 *        #####################     #####################
 *
 *   Where octothorpes represent the buildings, and the asterisks represent
 *   the floodwater. In this case, three units of floodwater accumulate.
 *   Helper functions used in this algorithm are declared here as well.
 * Copyright 2013 by Patrick Payne.
 *****************************************************************************/

/******************************************************************************
 * CONSTANTS:
 *****************************************************************************/ 

/*! @brief A sentinal value used to indicate that no such index exists. */
#define INVALID_INDEX -1

/******************************************************************************
 * PUBLIC FUNCTION DECLARATIONS:
 *****************************************************************************/ 

/*! @brief Calculates the total volume of floodwater that would accumulate in
 *      the passed in city. See file header for details.
 *  @param list The city, represented as an array.
 *  @param size The number of slots the city occupies.
 *  @return The number of units of floodwater accumulated.
 */
int FloodVolume(int *list, int size);


/*! @brief Determines the starting end of the next water accumulation region
 *     of the city, i.e. the leftmost edge of a basin.
 *  @param list The city, represented as an array.
 *  @param size The number of slots the city occupies.
 *  @param start The index to start the search at.
 *  @return The index of the next starting edge, INVALID_INDEX if none exist.
 */
int GetNextStartIndex(int *list, int size, int start);


/*! @brief Determines the end of the current water accumulation region
 *     of the city, i.e. the rightmost edge of a basin.
 *  @param list The city, represented as an array.
 *  @param size The number of slots the city occupies.
 *  @param start The index to start the search at.
 *  @return The index of the ending edge, INVALID_INDEX if none exist.
 */
int GetNextEndIndex(int *list, int size, int start);

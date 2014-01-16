/******************************************************************************
 * File: test_city_fill.c
 * Author: Patrick Payne
 * Date Created: Oct 14, 2013
 * Purpose: Tests the FloodVolume() routine defined in city_fill.c.
 * Copyright 2013 by Patrick Payne.
 *****************************************************************************/
extern "C" {
#include "city_fill.h"
}
#include "gtest/gtest.h"


/******************************************************************************
 * TEST THE HELPER FUNCTIONS:
 *****************************************************************************/ 

TEST(TestHelpers, GetNextStartIndex) {
  int test_city[] = {1, 2, 3, 0, 0, 4, 3, 2};
  
  // In this case the next start index is after the start index.
  EXPECT_EQ(2, GetNextStartIndex(test_city, 8, 0));
  EXPECT_EQ(2, GetNextStartIndex(test_city, 8, 1));

  // In this case the next start index is the starting index.
  EXPECT_EQ(5, GetNextStartIndex(test_city, 8, 5));
  EXPECT_EQ(6, GetNextStartIndex(test_city, 8, 6));

  // If we start at an invalid index, just return INVALID_INDEX.
  EXPECT_EQ(INVALID_INDEX, GetNextStartIndex(test_city, 8, INVALID_INDEX));
}


TEST(TestHelpers, GetNextEndIndex) {
  int test_city[] = {1, 2, 3, 0, 0, 4, 3, 2};
  
  // In this case the next end index is after the start index.
  EXPECT_EQ(2, GetNextEndIndex(test_city, 8, 0));
  EXPECT_EQ(5, GetNextEndIndex(test_city, 8, 2));

  // This basin has no ending; no water collects.
  EXPECT_EQ(INVALID_INDEX, GetNextEndIndex(test_city, 8, 5));
  EXPECT_EQ(INVALID_INDEX, GetNextEndIndex(test_city, 8, 6));

  // If we start at an invalid index, just return INVALID_INDEX.
  EXPECT_EQ(INVALID_INDEX, GetNextEndIndex(test_city, 8, INVALID_INDEX));

  // Test the case where the end of the current basin is not where we first
  // stop increasing.
  int test_city2[] = {1, 0, 2, 3, 3, 3, 4, 0};
  EXPECT_EQ(6, GetNextEndIndex(test_city2, 8, 0));

}

/******************************************************************************
 * TEST THE MAIN ALGORITHM:
 *****************************************************************************/ 

TEST(TestFloodVolume, NoWater) {
  // No water should collect, city is level.
  int test_city1[] = {1, 1, 1, 1, 1, 1, 1, 1};
  EXPECT_EQ(0, FloodVolume(test_city1, 8));

  // No water should collect, city is triangular.
  int test_city2[] = {1, 2, 3, 4, 3, 2, 1};
  EXPECT_EQ(0, FloodVolume(test_city2, 7));

  // No water should collect, city is a plateau.
  int test_city3[] = {1, 2, 3, 4, 4, 4, 3, 2, 1};
  EXPECT_EQ(0, FloodVolume(test_city3, 9));
}


TEST(TestFloodVolume, OneBasin) {
  // 6 units of floodwater should accumulate in the area between 3 and 4.
  int test_city1[] = {1, 2, 3, 0, 0, 4, 3, 2};
  EXPECT_EQ(6, FloodVolume(test_city1, 8));

  // 10 units of floodwater should accumulate in the area between the 5s.
  int test_city2[] = {0, 5, 0, 0, 5};
  EXPECT_EQ(10, FloodVolume(test_city2, 5));

  // 7 units of floodwater should accumulate in the area between 1 and 10.
  int test_city3[] = {1, 0, 0, 0, 0, 0, 0, 0, 10, 0};
  EXPECT_EQ(7, FloodVolume(test_city3, 10));
}


TEST(TestFloodVolume, TwoBasins) {
  // 3 units between 4 and 5, 4 units between 8 and 7.
  int test_city1[] = {1, 4, 3, 2, 5, 7, 8, 6, 6, 5, 7, 6, 3, 2, 2, 1};
  EXPECT_EQ(7, FloodVolume(test_city1, 16));

  // 2 units should accumulate.
  int test_city2[] = {0, 1, 0, 1, 0, 1, 0, 0, 0};
  EXPECT_EQ(2, FloodVolume(test_city2, 9));

  // 5 units should accumulate in each basin.
  int test_city3[] = {0, 1, 2, 0, 0, 1, 2, 2, 2, 1, 0, 0, 100};
  EXPECT_EQ(10, FloodVolume(test_city3, 13));
}

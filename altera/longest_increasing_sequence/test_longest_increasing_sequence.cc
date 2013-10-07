/******************************************************************************
 * File: test_LongestIncreasingSequence.cp
 * Author: Patrick Payne
 * Date Created: Oct 07, 2013
 * Purpose: To test the LongestIncreasingSequence routine.
 * Copyright 2013 by Patrick Payne.
 *****************************************************************************/

extern "C" {
#include "longest_increasing_sequence.h"
}
#include "gtest/gtest.h"

TEST(BasicFunctionality, EmptyList) {
  int test_list[4];
  EXPECT_EQ(0, LongestIncreasingSequence(test_list, 0));
}


TEST(BasicFunctionality, Singleton) {
  int test_list[4] = {1};
  EXPECT_EQ(1, LongestIncreasingSequence(test_list, 1));

  test_list[0] = 10;
  EXPECT_EQ(1, LongestIncreasingSequence(test_list, 1));
}


TEST(BasicFunctionality, LongerLists) {
  int test_list[30] = {1, 2, 3, 4};
  EXPECT_EQ(4, LongestIncreasingSequence(test_list, 4));

  test_list[0] = 10;
  EXPECT_EQ(3, LongestIncreasingSequence(test_list, 4));

  test_list[1] = 10;
  test_list[2] = 10;
  EXPECT_EQ(2, LongestIncreasingSequence(test_list, 4));


  // Test this algorithm for a case where we have multiple possible sequences.
  test_list[0] = 1;
  test_list[1] = 2;
  test_list[2] = 3;
  test_list[3] = 4;
  test_list[4] = -5;
  test_list[5] = -4;
  test_list[6] = -3;
  test_list[7] = -2;
  test_list[8] = -1;
  EXPECT_EQ(5, LongestIncreasingSequence(test_list, 9));

  test_list[4] = 5;
  EXPECT_EQ(5, LongestIncreasingSequence(test_list, 9));
}

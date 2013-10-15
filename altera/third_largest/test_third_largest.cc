/******************************************************************************
 * File: test_LongestIncreasingSequence.cp
 * Author: Patrick Payne
 * Date Created: Oct 07, 2013
 * Purpose: To test the LongestIncreasingSequence routine.
 * Copyright 2013 by Patrick Payne.
 *****************************************************************************/

extern "C" {
#include "third_largest.h"
}
#include "gtest/gtest.h"

TEST(ThirdLargest, BasicCase) {
  int test_list[30] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

  EXPECT_EQ(1, third_largest(test_list, 3));
  EXPECT_EQ(2, third_largest(test_list, 4));
  EXPECT_EQ(3, third_largest(test_list, 5));
  EXPECT_EQ(4, third_largest(test_list, 6));
  EXPECT_EQ(5, third_largest(test_list, 7));
  EXPECT_EQ(6, third_largest(test_list, 8));
  EXPECT_EQ(7, third_largest(test_list, 9));
}


TEST(ThirdLargest, SlightlyMoreComplicated) {
  int test_list[30] = {-10, 15, 10000, 3, 223, -9, 2234, -678, 789};
  EXPECT_EQ(-10, third_largest(test_list, 3));
  EXPECT_EQ(3, third_largest(test_list, 4));
  EXPECT_EQ(15, third_largest(test_list, 5));
  EXPECT_EQ(789, third_largest(test_list, 9));
}

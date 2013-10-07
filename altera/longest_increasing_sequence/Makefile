# The makefile for testing the longest increasing sequence code.
# Where to find user code.
USER_DIR = .

# Flags passed to the preprocessor.
CPPFLAGS += -I$(GTEST_DIR)/include/

# Flags passed to the C++ compiler.
CXXFLAGS += -g -Wall -Wextra

# Flags passed to the C compiler.
CCFLAGS += -g -Wall -Wextra -std=c99

# All tests produced by this Makefile.  Remember to add new tests you
# created to the list.
TESTS = test_longest_increasing_sequence.out

# All Google Test headers.  Usually you shouldn't change this
# definition.
GTEST_HEADERS = $(GTEST_DIR)/include/gtest/*.h \
                $(GTEST_DIR)/include/gtest/internal/*.h

# House-keeping build targets.

all : $(TESTS)

clean :
	rm -f $(TESTS) gtest.a gtest_main.a *.o

# Builds gtest.a and gtest_main.a.

# Usually you shouldn't tweak such internal variables, indicated by a
# trailing _.
GTEST_SRCS_ = $(GTEST_DIR)/src/*.cc $(GTEST_DIR)/src/*.h $(GTEST_HEADERS)

# For simplicity and to avoid depending on Google Test's
# implementation details, the dependencies specified below are
# conservative and not optimized.  This is fine as Google Test
# compiles fast and for ordinary users its source rarely changes.
gtest-all.o : $(GTEST_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GTEST_DIR) $(CXXFLAGS) -c \
            $(GTEST_DIR)/src/gtest-all.cc

gtest_main.o : $(GTEST_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GTEST_DIR) $(CXXFLAGS) -c \
            $(GTEST_DIR)/src/gtest_main.cc

gtest.a : gtest-all.o
	$(AR) $(ARFLAGS) $@ $^

gtest_main.a : gtest-all.o gtest_main.o
	$(AR) $(ARFLAGS) $@ $^

# Builds a sample test.  A test should link with either gtest.a or
# gtest_main.a, depending on whether it defines its own main()
# function.

longest_increasing_sequence.o : $(USER_DIR)/longest_increasing_sequence.c \
	                       $(USER_DIR)/longest_increasing_sequence.h $(GTEST_HEADERS)
	$(CC) $(CPPFLAGS) $(CCFLAGS) -c $(USER_DIR)/longest_increasing_sequence.c

test_longest_increasing_sequence.o : $(USER_DIR)/test_longest_increasing_sequence.cc \
                              $(USER_DIR)/longest_increasing_sequence.h \
					                    $(GTEST_HEADERS)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $(USER_DIR)/test_longest_increasing_sequence.cc

test_longest_increasing_sequence.out : longest_increasing_sequence.o \
	                              test_longest_increasing_sequence.o gtest_main.a
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -pthread $^ -o $@

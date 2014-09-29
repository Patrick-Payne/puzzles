/******************************************************************************
 * File: multiplication_table.c
 * Author: Patrick Payne
 * Date Created: Sep 27, 2014
 * Purpose: Prints out a multiplication table.
 * Copyright 2014 by Patrick Payne.
 *****************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<errno.h>
#include<stdbool.h>
#include<string.h>
#include<math.h>

/******************************************************************************
 * Static function declarations
 *****************************************************************************/

/* Converts a string to an int, if possible. Returns true on success. */
bool get_number(const char *input, int *value);

/* Gets the number of digits needed to represent a binary integer. */
int num_digits(int number);

/******************************************************************************
 * Main function code.
 *****************************************************************************/

int main(int argc, char *argv[]) {
  // First, validate the inputs.
  if (argc != 3) {
    printf("Usage: %s {integer} {Output file path}\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  // Turn the string version of the number into an integer.
  int input_num = 0;
  if (!get_number(argv[1], &input_num)) {
    printf("Invalid Integer: %s\n", argv[1]);
    exit(EXIT_FAILURE);
  }

  // Open the output file
  FILE *outfile = fopen(argv[2], "w");

  // Print the first line of the table into the file.
  int max_width = num_digits(input_num * input_num);
  max_width++;

  fprintf(outfile, "%*s", max_width, "");
  for (int i = 1; i <= input_num; i++) {
    fprintf(outfile, "%*d", max_width, i);
  }
  fprintf(outfile, "\n");

  // Now print out each of the rows in the table.
  for (int row = 1; row <= input_num; row++) {
    fprintf(outfile, "%*d", max_width, row);
    for (int col = 1; col <= input_num; col++) {
      fprintf(outfile, "%*d", max_width, row * col);
    }
    fprintf(outfile, "\n");
  }

  // close the output file
  fclose(outfile);

  exit(EXIT_SUCCESS);
}


/******************************************************************************
 * Static function definitions
 *****************************************************************************/

/* Converts a string to an int, if possible. Returns true on success. */
bool get_number(const char *input, int *value) {
  char *end_ptr = NULL;
  long long_num = strtol(input, &end_ptr, 10);
  if (errno != 0 || long_num < INT_MIN || long_num > INT_MAX) {
    return false;
  } else if ((end_ptr - input) < strlen(input)) {
    // Not WHOLE string was valid.
    return false;
  } else {
    *value = (int) long_num;
    return true;
  }
}


int num_digits(int number) {
    double log_number;
    if (number > 0) {
      log_number = log10((double) number);
      log_number += 1;
    } else if (number < 0) {
      log_number = log10((double) (-number));
      log_number += 2;
    } else { // number == 0
      log_number = 1.0;
    }

    return (int) ceil(log_number);
}

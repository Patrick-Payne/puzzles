#!/usr/bin/perl -w
# An implementation of the "earliest deadline first" scheduling algorithm, used
# to schedule independent tasks for a robot. The tasks are hardcoded into this
# file, since I don't know how to do file IO and string manipulation yet.

@list = (["T1", 4, 45],
         ["T2", 4, 48],
         ["T3", 5, 25],
         ["T4", 2, 49],
         ["T5", 5, 36],
         ["T6", 2, 31],
         ["T7", 7, 9],
         ["T8", 5, 39],
         ["T9", 4, 13],
         ["T10", 6, 17],
         ["T11", 4, 29],
         ["T12", 1, 19]);

# First we sort the list in order of increasing deadline.
@earliest_deadlines = sort { $a->[2] <=> $b->[2] } @list;

# Now we determine the total time required, and whether the deadlines passed.
$sum = 0;
foreach $action (@earliest_deadlines) {
  $sum += $action->[1];

  # See if we passed the deadline or not.
  if ($sum <= $action->[2]) {
    $pass = "PASS";
  } else {
    $pass = "FAIL";
  }

  print "$action->[0], $sum, $action->[2], $pass\n";
}

#!/usr/bin/env python3

'''
File: order_the_ages.py
Author: Patrick Payne
Description: Solves the "Order the Ages" puzzle using a brute force approach,
    which is appropriate given the small set of possible solutions.
THIS SOLUTION IS INCOMPLETE!!!
'''
import itertools

TOTAL_AGE = 135
CAROL_AGE = 40
TOMMY_AGE = 16
NAMES = ("Andrew", "Carol", "Jessica", "Luke", "Tommy")

class BrokenConstraintError(Exception): pass


###############################################################################
# Function Definitions
###############################################################################


def get_left(name, arrangement):
    """ Returns the name of the person sitting to the left. """
    current_index = arrangement.index(name)
    if current_index == 0:
        return arrangement[-1]
    else:
        return arrangement[current_index - 1]


def get_right(name, arrangement):
    """ Returns the name of the person sitting to the right. """
    current_index = arrangement.index(name)
    if current_index == (len(arrangement) - 1):
        return arrangement[0]
    else:
        return arrangement[current_index + 1]

def apply_age_difference(older_name, younger_name, age_difference, ages):
    """
    Applies an age difference constraint to the dictionary ages. If a
    dictionary entry exists for one of the ages but not the other, the entry
    for the other will be created to match the constraint. If neither exist,
    nothing is done. If both exist but violate the constraint, raise
    BrokenConstraintError. Age difference must be positive.
    """
    assert age_difference > 0, "Nonpositive age difference used."

    # Do nothing if neither age is known.
    if (older_name not in ages) and (younger_name not in ages):
        pass

    # If we have one but not the other, set the other to match constraints.
    elif (older_name not in ages) and (younger_name in ages):
        ages[older_name] = ages[younger_name] + age_difference

    elif (older_name in ages) and (younger_name not in ages):
        ages[younger_name] = ages[older_name] - age_difference

        # Make sure the age is positive.
        if ages[younger_name] <= 0:
            message = "{} has non-positive age.".format(younger_name)
            raise BrokenConstraintError(message)

    # If we have both, check that they obey constraints
    elif ages[older_name] - ages[younger_name] != age_difference:
        raise BrokenConstraintError("{} is not ".format(older_name)   +
                                    "{} years".format(age_difference) +
                                    "older than {}.".format(younger_name))


def is_arrangement_valid(arrangement):
    """Returns True if a seating arrangement meets the riddle constraints."""
    # Put in some of the hard constraints.
    ages = {"Carol": 40, "Luke": 16}

    try:
        # Carol is 12 years older than her neighbour to the left.
        person_left_of_carol = get_left("Carol", arrangement)
        apply_age_difference("Carol", person_left_of_carol, 12, ages)

        # Luke is 5 years younger than his neighbour to the left.
        person_left_of_luke = get_left("Luke", arrangement)
        apply_age_difference(person_left_of_luke, "Luke", 5, ages)

        # Keep trying to apply constraints until there is only one person left.
        # This is probably an infinite loop in some cases.
        while (len((ages.keys() - NAMES)) > 1):
            # Tommy is five years older than his neighbour to the right.
            person_right_of_tommy = get_right("Tommy", arrangement)
            apply_age_difference("Tommy", person_right_of_tommy, 5, ages)

            # Jessica is 14 years older than her neighbour to the left.
            person_left_of_jessica = get_left("Jessica", arrangement)
            apply_age_difference("Jessica", person_left_of_jessica, 14, ages)

    except BrokenConstraintError:
        return False

    # when only one person is left, their age can be determined from the
    # Maximum age of 135.
    last_name = (ages.keys() - NAMES).pop()
    last_age = 135
    for age in ages.items():
        last_age -= age
     
    ages[last_name] = last_age

    # The ages must be in order: Luke, Tommy, Andrew, Jessica, and Carol.
    return (ages["Luke"] < ages["Tommy"] < 
        ages["Andrew"] <  ages["Jessica"] < ages["Carol"])


def main():
    """The main program loop."""

    # Permutations() generates straight line permutations, so we will have
    # duplicated all roundtable permutations by a multiplicative factor of n,
    # where n is the number of seated occupants. This isn't a big deal in this
    # small problem.
    for permutation in itertools.permutations(NAMES):
        # Check these combinations against the constraints.
        if is_arrangement_valid(permutation):
            # Print out the correct answer when found.
            print(permutation)
            return 0

if __name__ == '__main__':
    main()

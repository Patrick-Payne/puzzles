'''
File: get_shortest_substring.py
Author: Patrick Payne
Description: Given a string and a list of letters, get the shortest substring
    that contains all of the letters.
'''


class NoSubstringFound(Exception):
    """
    Raised when there is no valid substring containing all of the letters
    """
    pass


def get_indices(letters, searched_string):
    """
    Given a container with letters and a string, return a two-tuple. The
    first element is a list of all indices of the string containing matching
    letters. The second element is a dictionary of string indices by letter,
    with the keys being the letters searched for, and the values being lists of
    indices containing that letter. This function is case sensitive.
    """
    # Create empty lists for the indices of each letter.
    indices_by_letter = {}
    for letter in letters:
        indices_by_letter[letter] = []

    all_indices = []
    for index, letter in enumerate(searched_string):
        if letter in letters:
            # Appending in this fashion ensures that the indices are sorted.
            all_indices.append(index)
            indices_by_letter[letter].append(index)

    return all_indices, indices_by_letter


def max_starting_index(indices_by_letter):
    """
    Given a dictionary with keys being characters, and the values being lists
    of string indices containing thouse letters, determine the maximum starting
    index of a substring containing all of the letters. If no such substrings
    are possible, raise a NoSubstringFound exception.
    """
    max_start_index = None
    for letter, indices in indices_by_letter.items():
        # We can't make any substring containing all letters if a letter is not
        # actually in the searched string.
        if indices == []:
            raise NoSubstringFound("'{0}'".format(letter) +
                                   " was not found in the searched string.")

        # Any substring must start at/before the last index with this letter.
        max_for_letter = max(indices)
        if (max_start_index is None) or (max_for_letter < max_start_index):
            max_start_index = max_for_letter

    return max_start_index


def next_index(min_index, indices):
    """
    Given a list of indices sorted from smallest to largest, return the next
    index in the list that is greater than min_index.
    """
    # We use an iterative implementation of binary search.
    left = 0
    right = len(indices) - 1
    assert indices[right] >= min_index, "No greater index found."

    # Keep narrowing the list until we know where the next greater index is.
    while right - left > 1:
        middle = left + (right - left) // 2
        middle_index = indices[middle]

        if middle_index > min_index:
            right = middle
        else:
            left = middle

    # Now we are only searching between two elements, at left and right.
    if indices[left] > min_index:
        return indices[left]
    else:
        return indices[right]


def get_shortest_substring(letters, searched_string):
    """
    Given a container of letters and a string, return the shortest substring
    that contains all of the letters. Case sensitive.
    """
    # If there are no letters, we return the empty string.
    if len(letters) == 0:
        return ''

    # Eliminate any duplicate letters.
    letters = set(letters)

    # Extract the indices of the matching letters from the searched string.
    indices, indices_by_letter = get_indices(letters, searched_string)
    max_start_index = max_starting_index(indices_by_letter)

    # Find the substring starting at each matching letter, and see if it is
    # the shortest.
    smallest_string = None
    for start_index in indices:
        # Don't bother to continue searching if no more substrings exist.
        if start_index > max_start_index:
            break

        # Find the indices of the other letters after this start index.
        indices_of_next_letters = []
        for letter in (letters - {searched_string[start_index]}):
            closest_letter = next_index(start_index,
                                        indices_by_letter[letter])
            indices_of_next_letters.append(closest_letter)

        # If only one letter is searched for, then the result is 1 letter long.
        if indices_of_next_letters == []:
            end_index = start_index

        # Otherwise, finish the string at the last of the other letters.
        else:
            end_index = max(indices_of_next_letters)

        current_substring = searched_string[start_index:end_index + 1]
        if smallest_string is None:
            smallest_string = current_substring
        elif len(current_substring) < len(smallest_string): 
            smallest_string = current_substring

    return smallest_string

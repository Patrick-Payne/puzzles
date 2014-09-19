#!/usr/bin/env python3
from sys import argv

def get_all_permutations(char_list):
    # Base case: there is only one permutation of 1 character.
    if len(char_list) == 1:
        return [char_list[0]]
    
    # Approach: Recursively select the first character of the permutation,
    # and prepend that to the each of the permutations of the rest of the chars.
    # return the unique permutations.
    unique_results = set()
    for index, char in enumerate(char_list):
        remaining_chars = char_list[:index] + char_list[index + 1:]
        permutations_of_rest = get_all_permutations(remaining_chars)
        unique_results |= {char + permutation for permutation in permutations_of_rest}

    return unique_results
        

if __name__ == '__main__':
    if len(argv) > 1:
        print("\n".join(get_all_permutations(list(argv[1]))))

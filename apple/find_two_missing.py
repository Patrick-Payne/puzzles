#!/usr/bin/env python3

def find_two_missing(numbers, N):
    assert len(numbers) == N - 2
    # Use None as a dummy value in our pseudo-bucket sort.
    numbers.append(None)
    numbers.append(None)

    # If a valid number is in the wrong slot, swap it.
    for index in range(len(numbers)):
        if numbers[index] != None and numbers[index] != index + 1:
            swap(numbers, index, numbers[index] - 1)

    # Use None to represent that we haven't found the missing numbers yet.
    first_num = None
    second_num = None
    for index in range(len(numbers)):
        # Find where the sentinal values ended; those are the missing numbers.
        if numbers[index] == None:
            if first_num == None:
                first_num = index + 1
            else:
                second_num = index + 1


    # Remove the sentinal values from the final sorted list.
    numbers.pop(second_num - 1)
    numbers.pop(first_num - 1)

    return (first_num, second_num)

def swap(numbers, index1, index2):
    temp = numbers[index1]
    numbers[index1] = numbers[index2]
    numbers[index2] = temp
    return

if __name__ == '__main__':
    numbers = [4, 3 , 2, 1]
    assert find_two_missing(numbers, 6) == (5, 6)

    numbers = [6, 2 , 1, 5]
    assert find_two_missing(numbers, 6) == (3, 4)
    


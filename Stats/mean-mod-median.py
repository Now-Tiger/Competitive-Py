#!/usr/bin/env

from __future__ import division, annotations
import numpy as np

# what are the largest and smallest values => ( min, max )
# first I will sort the array/list
# mean of the data:
# median of the data: here data should be in sorted manner.


def mean(array: np.ndarray) -> None:
    # total = 0
    # for i in array :
    #     total += i
    # return total / len(array)         <<= for loop is costly...
    # return sum(array) / len(array)
    return np.average(array)


def median(array: np.ndarray) -> None:
    n = len(array)
    sorted_array = sorted(array)
    midpoint = n // 2

    # if length of lis is odd: just return mid value
    if n % 2 == 1:
        return sorted_array[midpoint]
    else:
        # if list is even then return average :
        low = midpoint - 1
        high = midpoint
        return (sorted_array[low] + sorted_array[high]) / 2


if __name__ == "__main__":
    num_friends = np.array([100, 49, 40, 25, 41, 29, 60, 55])
    sorted_numbers = sorted(num_friends)
    print(sorted_numbers)
    # print(f"minimum element: {sorted_numbers[0]}")
    # print(f"maximum element: {sorted_numbers[-1]}")
    # print(f"second largest element: {sorted_numbers[-2]}")
    print(f"mean: {mean(num_friends)}")
    print(f"median: {median(num_friends)}")

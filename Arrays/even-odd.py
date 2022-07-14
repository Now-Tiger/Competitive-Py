#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

# Problem:
# given an array of integers, you have to reorder the elements so that the even integers appears first.
# You have to solve this without using any extra space/storage.

# ---------------------------------------------------------------

# Approach:
# We can partition the array into three subarrays: Even, Unclassified and Odd, appearing in that order.
# Initially Even and Odd are empty Unclassified is the entire array. 
# We iterate through Unclassified, moving its elements to the boundaries of the Even and Odd
# subarrays via swaps, thereby expanding Even and Odd, and shrinking Unclassified.

# ---------------------------------------------------------------

from __future__ import annotations, division

def even_odd(array: list) -> list:
    next_even, next_odd = 0, len(array) - 1
    while next_even < next_odd:
        if array[next_even] % 2 == 0:
            next_even += 1
        else:
            array[next_even], array[next_odd] = array[next_odd], array[next_even]
            next_odd -= 1
    return array

a = [1, 0, 5, 3, 6, 2, 4, 7, 9]
print(even_odd(a))


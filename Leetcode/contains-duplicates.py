#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

"""
 ********************************************************* Contains Duplicate *********************************************************

Problem: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element 
         is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

"""


class Solution:
    def brute_force(self, array: list) -> bool:
        """
        The bruteforce algorithm: We can iterate over all pairs of numbers, 
        then compare for equality. This takes O(N^2) quadric time, at the cost of a constant space.
        """
        for i in range(len(array)):
            for j in range(i):
                if array[i] == array[j]:
                    return True
        return False

    def sort_and_check(self, array: list) -> bool:
        """ 
        complexity is improved to O(N LogN) and we 
        are still using the O(1) constant space.
        """
        array.sort()
        for i in range(len(array)):
            if array[i] == array[i - 1]:
                return True
        return False

    def contains_duplicate_optimised(self, array: list):
        return not len(array) == len(set(array))


if __name__ == '__main__':
    array = [1, 2, 3, 0, 0, 4, 6, 5]
    class_instance = Solution()

    res = Solution.contains_duplicate_optimised(class_instance, array)
    if res == True:
        print('YES : Duplicate elements found !')
    else:
        print('Does not contain duplicates.')


# $ python contains-duplicates.py
# YES : Duplicate elements found !

#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

# Python program to find N largest elements from a list.
# Given a list of integers, the task is to find N largest elements assuming
# size of list is greater than or equal o N.

# Examples :
# Input : [4, 5, 1, 2, 9],  N = 2
# Output :  [9, 5]

# Input : [81, 52, 45, 10, 3, 2, 96],  N = 3
# Output : [81, 96, 52]

# -------------------------------------------------------------------------

from __future__ import annotations


class Solution(object):
    def nlargest_elements(self, array: list, n: int) -> list:
        """
            Time complexity: O(n * size)
            size = size of given list
            S.C = O(n) extra space is used to store largest 
            elements
        """
        final = []
        for _ in range(n):
            largest = 0
            for j in range(len(array)):
                if array[j] > largest:
                    largest = array[j]
            array.remove(largest)
            final.append(largest)
        print(final)
        return

    def nlargests(self, array: list, n: int) -> int:
        """
            T.C = O(n * size)
            S.C = O(1) no extra space is used to 
            store largest elemets
        """
        for _ in range(n):
            largest = 0
            for j in range(len(array)):
                if array[j] > largest:
                    largest = array[j]
            print(largest, end=", ")
            array.remove(largest)
        return


if __name__ == "__main__":
    array = [1, 222, 21, 33, 452, 111]
    n = 3
    instance = Solution()
    Solution.nlargests(instance, array, n)

# $ pypy3 Arrays/n-largest-elements.py 
# 452, 222, 111,
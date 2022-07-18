#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

# ------------------------------- 215. Kth Largest Element in an Array -------------------------------
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# ---------------------------------------------------------------------------------------------------

from __future__ import annotations
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


if __name__ == "__main__":
    array = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    instance = Solution()
    print(Solution.findKthLargest(instance, array, k))

# $ pypy3 leetcode/kth-largest-element.py
# 4

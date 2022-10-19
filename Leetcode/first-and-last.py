#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---------------------------------- Find First and Last Position of Element in Sorted Array --------------------------------------

# Problem statement : Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a 
#                     given target value.
#                     If target is not found in the array, return [-1, -1].
#                     You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
# --------------------------------------------------------------------------------------------------------------------------------


class Solution(object):
    def searchRange(self, nums: list, target: int) -> list:
        def binarysearch(self, nums: list, target: int) -> int:
            left = 0
            right = len(nums)
            while (left < right):
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left

        left = binarysearch(self, nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = binarysearch(self, nums, target + 1)
        return [left, right - 1]

    def time_optimized(self, nums: list, target: int) -> list:
        first = -1
        last = -1
        for i in range(len(nums)):
            if target != nums[i]:
                continue
            if first == -1:
                first = i
            last = i
        if first != -1:
            return [first, last]
        return [first, last]


if __name__ == '__main__':
    # Example 1:
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    instance = Solution()
    print(Solution.searchRange(instance, nums, target))

    # Example 2 :
    nums = [5, 7, 8, 8, 7, 8, 10]
    target = 8
    print(Solution.time_optimized(instance, nums, target))


# $ pypy3 first-and-last.py
# [3, 4]
# [2, 5]

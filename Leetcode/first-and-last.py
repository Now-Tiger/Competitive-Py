#!/usr/bin/env python3

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

from typing import List

class Solution :
    def searchRange(self, nums : List[int], target : int) -> List[int] :
        left : int = 0
        right : int = len(nums) - 1
        start : int = -1
        end : int = -1
        
        while left <= right :
            mid : int = (left + right ) // 2
            if target == nums[mid] :
                start = mid
                right = mid - 1
            elif target < nums[mid] :
                right = mid - 1
            else :
                left = mid + 1
        if start == -1 :
            return -1, -1
        
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid : int = (left + right) // 2
            if target == nums[mid] :
                end = mid
                left = mid + 1
            elif target < target :
                right = mid - 1
            else :
                left = mid + 1
        return start, end 

if __name__ == '__main__' :
    # Example 1 :
    # nums = [5,7,7,8,8,10], target = 8
    nums : List[int] = [5, 7, 7, 8, 8, 10]
    target : int = 8
    print(Solution.searchRange(Solution, nums, target))

    # Example 2 :
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(Solution.searchRange(Solution, nums, target))

    print('\n---------------------------\n')

# -------------------------------------------------------------------------------------------------------------------------------

class Solution :
    def firstLast(self, nums : List[list], target : int) -> List[int] :
        first : int = -1
        last : int = -1
        for i in range(len(nums)) :
            if target != nums[i]  :
                continue
            if first == -1 :
                first = i
            last = i
        if first != -1 :
            return first, last
        return first, last

if __name__ == '__main__' :
    nums : List[int] = [5, 7, 7, 8, 8, 10]
    target : int = 8
    print(Solution.firstLast(Solution, nums, target))

    nums : List[int] = [5, 7, 7, 8, 8, 10]
    target : int = 6
    print(Solution.firstLast(Solution, nums, target))

# $ python first-and-last.py 
# (3, 4)
# (-1, -1)
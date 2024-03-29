#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

# problem:  Given an array of integers nums and an integer target, return indices of the two numbers such that 
#            they add up to the target.
#            You may assume that each input would have exactly one solution, and you may not use the same element twice.
#            You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List


class Solution:
    """
        This solution is inefficient.
        Time complexity is O(n^2)
        the reason is two loops / nested loop
    """
    def two_sum_naive(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return []
    
    
    def two_sum_binary_search(self, nums: List[int], target: int) -> List[int]:
        """
        This one is better than the previous one.
        We have sorted the array in ascending order
        and used only a single loop over the elements.
        Time complexity is O(nlogn)
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return [left, right]
            elif total < target:
                left += 1
            else:
                right -= 1
        return []        


    def two_sum_hasmap(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            remaining =  target- num
            if remaining in dict :
                return[i,  dict[remaining]]
            else :
                dict[num] = i


if __name__ == "__main__" :
    array = [1, 2, 3, -7, -5]
    target = -12
    instance = Solution()
    res = Solution.two_sum_hasmap(instance, array, target)
    print(res)

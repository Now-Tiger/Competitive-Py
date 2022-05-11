#!/usr/bin/ pypy3

# problem :  Given an array of integers nums and an integer target, return indices of the two numbers such that 
#            they add up to target.
#            You may assume that each input would have exactly one solution, and you may not use the same element twice.
#            You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# ----------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    """
        This solution is inefficient.
        Time complexity is O(n^2)
        resons is two loops / nested loop
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return []

# ----------------------------------------------------------------

class Solution:
    """
        This one is better than the previous one.
        We have sorted the array in ascending order
        and used only single loop over the elements.
        Time complexity is O(nlogn)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return [nums[left], nums[right]]
            elif total < target:
                left += 1
            else:
                right -= 1
        return []        

# ----------------------------------------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
    res = Solution.twoSum(instance, array, target)
    print(res)
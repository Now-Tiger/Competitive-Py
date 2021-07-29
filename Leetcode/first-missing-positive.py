'''
problem : Given an unsorted integer array nums, return the smallest missing positive integer.
          You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:

Input: nums = [1,2,0]
Output: 3

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
'''

def firstMissingPositive(nums):

        # base condition :
        if not nums: return 1
        nums2 = [False] * (len(nums) + 1)

        for num in nums:
            if 0 < num <= len(nums):
                nums2[num] = True
        
        for i in range(1, len(nums2)):
            if not nums2[i]:
                return i
 
        if not nums2:
            return 1
        return len(nums2)

nums = [3,4,-1,1]
print(firstMissingPositive(nums))
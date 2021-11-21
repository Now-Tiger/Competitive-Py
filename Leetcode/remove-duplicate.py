# ---------------------------------------------------- Remove Duplicates from Sorted Array ----------------------------------------------------

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of 
# the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final 
# result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# --------------------------------------------------------------------------------------------------------------------------------------------- 

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int : 
        n = len(nums) 
        previous = nums[0]
        index = 1
        length = 1
        if n == 0 : return 0;
        for i in range(n) :
            if nums[i] != previous :
                length += 1
                previous = nums[i]
                nums[index] = nums[i]
                index += 1
        return length
    
# ---------------------------------------------------------------------------------------------------------------------------------------------

# This code is not efficient one; gives error when provided an edge case such : [1, 1]
# but works fine on large array-consist of numbers.
# You can use this solution as a naive solution and tell that this isn't a great solution and can implement 
# another solution that is mentioned above.

class Solution : 
    def removeduplicates(arr, n) :
        # base condition :
        if n == 0 | n == 1 :
            return n 
        temp = list(range(n))
        j = 0
        for i in range(n-1) :
            if arr[i] != arr[i + 1] :
                temp[j] = arr[i]
                j += 1
        temp[j] = arr[n - 1]
        j += 1
        # modify the array :
        for i in range(0, j) :
            arr[i] = temp[i]
        return j
    
if __name__ == '__main__' :
    # For first Solution : 
    nums = [1, 1]
    instance = Solution()
    print(Solution.removeDuplicates(instance, nums))
    
    # For second Solution :
    arr = [0,0,1,1,1,2,2,3,3,4]
    n = len(arr)
    n = Solution.removeduplicates(arr, n)
    # Print updated array
    for i in range(n):
        print("%d" % (arr[i]), end=" ")

# $ python remove-duplicate.py 
# 1
# 0 1 2 3 4 

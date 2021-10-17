
# ------------------------------------------------------ Sort Colors ------------------------------------------------------ 
#
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color 
# are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
#
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
# -------------------------------------------------------------------------------------------------------------------------

class Solution(object) :
    def sortColors(self, nums) :
        left = curr = 0
        right = len(nums) - 1
        while curr <= right :
            if nums[curr] == 0 :
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2 :
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else :
                curr += 1
        return nums
            

if __name__ == '__main__' :
    A = [2,0,2,1,1,0]
    instance = Solution()
    res = Solution.sortColors(instance, A)
    print(f'Sorted color list : {res}')

    # example 2
    B = [2,0,1]
    print(f'Sorted color list : {Solution.sortColors(Solution, B)}')

# $ python sort-colors.py 
# Sorted color list : [0, 0, 1, 1, 2, 2]
# Sorted color list : [0, 1, 2]
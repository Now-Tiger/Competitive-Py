
# ------------------------------------------------- Maximum Subarray -------------------------------------------------

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum 
# and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6


# Example 2:

# Input: nums = [1]
# Output: 1
# --------------------------------------------------------------------------------------------------------------------

class solution : 
    # Using Kaden's Algorithm here :
    def maxsubarray(array) :
        size = len(array)
        max_so_far = array[0]
        curr_max = array[0]

        for i in range(1, size) :
            curr_max = max(array[i], curr_max + array[i])
            max_so_far = max(max_so_far, curr_max)
        print( max_so_far )


if __name__ == '__main__' :
    A = [-2,1,-3,4,-1,2,1,-5,4]
    res = solution.maxsubarray(A)
    res

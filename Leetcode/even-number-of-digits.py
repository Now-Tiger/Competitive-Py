#!/usr/bin/env python3

# --------------------------------------- Find Numbers with Even Number of Digits ---------------------------------------

# Given an array nums of integers, return how many of them contain an even number of digits.

# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
#
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
#
# Example 2:
# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.
# 
# -----------------------------------------------------------------------------------------------------------------------

from typing import List
class Solution :
    def findNumber(self, nums : List[int]) -> List[int] :
        count : int = 0
        for i in nums:
            if len(str(i)) % 2 == 0 :
                count += 1
        return count

if __name__ == '__main__' :
    # Example 1:
    arr = [12, 345, 2, 6, 7896]
    print(Solution.findNumber(Solution, arr))

    # Example 2 :
    arr = [555, 901, 482, 1771]
    print(Solution.findNumber(Solution, arr))


# $ python even-number-of-digits.py 
# 2
# 1

# T.C = O(n)
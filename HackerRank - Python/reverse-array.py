#!/usr/bin/env cython

from __future__ import print_function
import cython

@cython.cfunc
def reverseList(nums : cython.int, 
                startIndex : cython.int, 
                endIndex : cython.int) -> cython.int :
    
    if len(nums) is None :
        return nums
         
    while startIndex < endIndex :
        nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]
        startIndex += 1
        endIndex -= 1

if __name__ == '__main__' :
    nums : cython.int = [1, 2, 3]
    reverseList(nums, 0, 2)
    print(nums)

# $ python Cython/reverse-array.py 
# [3, 2, 1]

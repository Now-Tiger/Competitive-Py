'''
******************* Largest Sum Contiguous Subarray ******************** 

problem :  Write an efficient program to find the sum of contiguous subarray 
           within a one-dimensional array of numbers that has the largest sum. 

this question is same as the kaden's algo, but in this case we'll return starting point
and ending point of subarray from which we have got maximum sum.

'''
from sys import maxsize

def maxsub_array_sum(A, size) :
    max_so_far = -maxsize - 1 
    max_ending_here = 0 
    start, end, s = 0, 0, 0

    for i in range(0, size) :
        max_ending_here += A[i]

        if max_ending_here < 0 :
            max_ending_here = 0
            s = i + 1

        if max_so_far < max_ending_here :
            max_so_far = max_ending_here 
            start = s
            end = i

    return max_so_far, start, end

A = [11, 12, 5, -9, -8, 1, 2]
print(maxsub_array_sum(A, len(A)))
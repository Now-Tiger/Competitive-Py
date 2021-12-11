#!/usr/bin/env python3

# Problem : Given a sorted array arr[] and a number x, write a function that 
#           counts the occurrences of x in arr[]. Expected time complexity 
#           is O(Logn)

# ---------------------------- Naive approaches ---------------------------- 

# 1. Creating our own function :

from typing import List
from collections import Counter

def count_occurrences(lis : List[int], key : int) -> int :
    counter : int = 0
    for i in lis :
        if key not in lis :
            return key
        elif key == i :
            counter += 1
        else :
            continue
    return counter 

# eg.
lis = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8]
print(count_occurrences(lis, 5))    
# 3                 <= output

# ------------------- using built in count() function ----------------------

nums : List[int] = [5, 6, 7, 8, 9, 10, 11, 11, 11, 12, 15, 15]
print(nums.count(11))

# ------------------- using Counter from collections -----------------------

key = 8
count = Counter(lis)
print(count[key])

# -------------------------------- Optimized -------------------------------

def binarysearch(A, left, right, x):
    if left > right :
        return -1
    mid = int(left+(right-left)/2)
    if A[mid] == x :
        return mid
    if x < A[mid] :
        return binarysearch(A, left, mid-1, x)
    return binarysearch(A, mid+1, right, x)

def countoccurrences(A, n, x):
    ind = binarysearch(A, 0, n-1, x)
    if ind == -1 : # Base condition
        return 0
    count = 1

    # count elements on left side :
    left = ind - 1
    while left >= 0 and A[left] == x :
        count +=1
        left = left - 1

    # count elements on right side :
    right = ind + 1
    while right < n and A[right] == x :
        count +=  1
        right += 1
    return count

if __name__ == '__main__' :
    A = [1, 2, 3, 5, 8, 8, 9, 9, 9, 9, 15]
    x = 8
    n = len(A)
    print("Occurance of key",x,"is",countoccurrences(A,n,x),'times.')

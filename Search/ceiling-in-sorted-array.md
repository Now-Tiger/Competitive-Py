# Ceiling in a sorted array 
### Problem statement :
 Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x, 
 and the floor is the greatest element smaller than or equal to x. Assume than the array is sorted in non-decreasing order. 
 Write efficient functions to find floor and ceiling of x.
 
### Examples : 
- For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
- For x = 0:    floor doesn't exist in array,  ceil  = 1
- For x = 1:    floor  = 1,  ceil  = 1
- For x = 5:    floor  = 2,  ceil  = 8
- For x = 20:   floor  = 19,  ceil doesn't exist in array
``` python
def ceil(A, key) :
    (left, right) = (0, len(A)-1) 
    while left <= right :
        mid = (left + right) // 2
        if key == A[mid] :
            return mid
        elif key < A[mid] :
            right = mid - 1
        else :
            left = mid + 1
    return left


if __name__ == '__main__' :
    A = [1, 3, 5, 8, 10, 12]
    key = 7
    index = ceil(A, key)
    print(f'ceil of key {key} is {A[index]}')
   

# $ python ceiling-sorted-array.py 
# ceil of key 7 is 8

# T.C = O(logn)

# The above program is not complete yet, cause if we provide large number of value as a key, 
# then we get errors : IndexError,
# We should provide/raise IndexError in the program itself when someone provides higher value to search in
# the given search-space.
```

'''
    Problem : Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
    Input : A = [2, 5, 6, 8, 9, 10]
            target value = 5
    Output : 1   
    Explanation : Because target value 5 is present on index 1
'''

# Function to find target value through a sorted list of elements.  
def binary_search(A, x):
    (left, right) = (0, len(A)-1)
    while left <= right :
        # Find the mid-value in the search spance i.e list
        # and compare with target
        mid = (left + right) // 2

        # key = mid      key = target.
        if x == A[mid]:
            return mid
        
        # if key/target is smaller than the mid value
        # then search in left space,
        # exclude mid value
        elif x < A[mid]:
            right = mid - 1

        # if target is greater, then search through right
        # exclude mid
        # i.e include mid in left side.
        else :
            left = mid + 1
    return -1

# Driver code to run above function.
A = [2, 5, 6, 8, 9, 10]
key = 5
index = binary_search(A, key)

if index != -1:
    print('Element found at index', index)
else :
    print('Element does not exist in the list.')

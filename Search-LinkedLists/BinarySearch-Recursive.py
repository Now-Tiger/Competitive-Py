# Recursive implementation of the binary search algorithm to return
# the position of target `x` in subarray `A[left…right]`

def binary_search(A, left, right, x):
    # base condition element not in the list.
    if left > right :
        return - 1          

    mid = (left + right)//2

    if x == A[mid]:
        return mid

    elif x < A[mid]:
        return binary_search(A, left, mid -1, x)
    else :
        return binary_search(A, mid + 1, right, x)

# Driver code :
if __name__ == '__main__' :
    A = [2, 5, 6, 8, 9, 10]
    key = 9

    (left, right) = (0, len(A)- 1)
    index = binary_search(A, left, right, key)

    if index != 1:
        print('Element found at the index', index)
    else :
        print('Element does not exist')
        
        
        
        

'''
Problem : Given a sorted array arr[] and a number x, write a function that counts the occurrences of x 
          in arr[]. Expected time complexity is O(Logn)
'''
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
        count = count+ 1
        left = left - 1

    # count elements on right side :
    right = ind + 1
    while right < n and A[right] == x :
        count = count + 1
        right = right + 1
    return count

# Driver code :
A = [1, 2, 3, 5, 8, 8, 9, 9, 9, 9, 15]
x = 8
n = len(A)
print("Occurance of key",x,"is",countoccurrences(A,n,x),'times.')

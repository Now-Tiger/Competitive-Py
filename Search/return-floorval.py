'''
Problem : Given a sorted array and a value x, the floor of x is the largest element in array smaller 
          than or equal to x. Write efficient functions to find floor of x.
'''
def floorsearch(arr, left, right, x):
    # Base condition :
    if left > right :
        return -1
    if x > arr[right] :
        return right
    
    # mid position formula :
    mid = int(left + (right - left)/2)
    if arr[mid] == x :
        return mid
    
    # if x is present in between mid-1 & mid :
    if mid > 0 and arr[mid-1] <= x and x < arr[mid] :
        return mid-1

    # if x is smaller than mid :
    if x < arr[mid] :
        return floorsearch(arr, left, mid-1, x)
    return floorsearch(arr, mid+1, right, x)

A = [1, 2, 3, 5, 8, 9, 15, 22, 30]
x = 18
(left, right) = (0, len(A)-1)
index = floorsearch(A, left, right, x)
if index != -1 :
    print("Floor value of", x,"is", A[index])
else :
    print("Floor value does not exist")

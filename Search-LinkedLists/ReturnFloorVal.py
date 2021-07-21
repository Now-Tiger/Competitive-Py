'''
    Problem statement : Given a sorted array and a value x, the floor of x is the largest element in 
                        array smaller than or equal to x. Write efficient functions to find floor of x.
    
    Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 20
    Output : 19
    19 is the largest element in
    arr[] smaller than 20.

    Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 0
    Output : -1
    Since floor doesn't exist,
    output is -1.

'''
def floorsearch(A, left, right, x):
    
    # if left value is greater than right values.
    # that shouldn't be possible in sorted array :
    if left > right :
        return -1
    
    # if key is greater than right value, return high value
    if x > A[right]:
        return right

    # if key found at mid then return mid index :
    # formula to calculate mid.
    mid = int(left + (right - left) / 2)      
    if A[mid] == x :
        return mid

    # If x lies between mid-1 and mid
    if mid >0 and A[mid - 1] <= x and x < A[mid]:
        return mid - 1
    
    # if key is smaller than mid, move to left space; else...right
    if x < A[mid]:
        return floorsearch(A, left, mid - 1, x)
    return floorsearch(A, mid+1, right, x)


# Driver Code
A = [1, 2, 4, 6, 10, 12, 14]
n = len(A)
x = -1
index = floorsearch(A, 0, n-1, x)
 
if (index == -1):
    print("Floor of", x, "doesn't exist\
                    in array ", end = "")
else:
    print("Floor of", x, "is", A[index])
    
    
    

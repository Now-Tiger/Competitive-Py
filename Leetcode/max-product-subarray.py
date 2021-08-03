# ------------------------------ Maximum Product Subarray -------------------------------------------------
# Problem : Given an array Arr that contains N integers (may be positive, negative or zero). Find the product 
#           of the maximum product subarray.

'''
Example 1:

Input:
N = 5
Arr[] = {6, -3, -10, 0, 2}

Output: 180

Explanation: Subarray with maximum product
is 6, -3, -10 which gives product as 180.'''

def maxProd(arr, n) :
    maxVal = arr[0]
    minVal = arr[0]
    maxProduct = arr[0]

    for i in range(1, n, 1) :
        if arr[i] < 0 :
            temp = maxVal 
            maxVal = minVal
            minVal = temp
        maxVal = max(arr[i], maxVal * arr[i])
        minVal = min(arr[i], minVal * arr[i])
        maxProduct = max(maxProduct, maxVal)
    return maxProduct

arr = [1, 2, -3, 8, 1]
print(maxProd(arr, 5))

# T.c = O(n) ; space = O(1)




# 1. Reversing array elements from start to end : iterative process.
# input : arr[] = [1, 2, 3, 4, 5, 6]
# output : arr[] = [6, 5, 4, 3, 2, 1]

# python function to reverse an array. 
def RevrsArray(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
# Drive function to reverse the array:
A = [1, 2, 3, 4, 5, 6]
print(A)
RevrsArray(A, 0, 5)
print(A)

A = [3, 2, 1, 0, -1, -2]
print(A)
RevrsArray(A, 0, 5)
print(A)

# Method 2 : Reversing list by slicing.
def RevsList(A):
    print(A[::-1])

A = [4, 3, 2, 1, 0]
print('Original List')
RevsList(A)
print('Reversed list :', A)


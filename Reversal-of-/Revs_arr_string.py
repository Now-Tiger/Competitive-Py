# input : arr[] = [1, 2, 3, 4, 5, 6]
# output : arr[] = [6, 5, 4, 3, 2, 1]

# Iterative process to reverse the entire array string/list
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
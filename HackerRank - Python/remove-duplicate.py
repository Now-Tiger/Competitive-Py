# Remove Duplicates from Sorted Array

def removeduplicates(arr, n) :
    # base condition :
    if n == 0 | n == 1 :
        return n 
    # create new array of same length :
    # where we can save unique values.
    temp = list(range(n))
    j = 0

    for i in range(n-1) :
        # if the next value is not equal
        # then save current value in temp.
        if arr[i] != arr[i + 1] :
            temp[j] = arr[i]
            j += 1

    # since we have not looked last value :
    temp[j] = arr[n - 1]
    j += 1

    # modify the array :
    for i in range(0, j) :
        arr[i] = temp[i]
    return j

# Driver code
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
n = len(arr)
# removeDuplicates() returns
# new size of array.
n = removeduplicates(arr, n)

# Print updated array
for i in range(n):
    print("%d" % (arr[i]), end=" ")

# ------------------------------- Find the missing number in an array without using any extra space -------------------------------

# You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. 
# One of the integers is missing in the list. Write an efficient code to find the missing integer.


# Input:  { 3, 2, 4, 6, 1 }
# Output: The missing element is 5
 
# Input:  { 3, 2, 4, 5, 6 }
# Output: The missing element is 1
 
# Input:  { 3, 2, 4, 5, 1 }
# Output: The missing element is 6


def findmissing(arr) :
    n = len(arr)
    total = sum(arr) 
    return (n + 1) + n * (n + 1) // 2 - total


if __name__ == '__main__' :
    arr = [3, 4, 6, 1, 5]
    print(f'Missing value is : {findmissing(arr)}')


# $ python find-missing.py 
# Missing value is : 2

# T.C = O(n),     S.C = O(1)



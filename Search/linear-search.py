'''
Problem: Given an array arr[] of n elements, write a function to 
search a given element x in arr[].

Examples :  

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
taregt :    x = 110;
Output : 6
Element x is present at index 6
'''
def linear_search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

# Driver code 
arr = [2, 40, 10, 3, 30]
x = 30
n = len(arr)

# Function call
result = linear_search(arr, n, x)
if result != -1:
    print('Element found at index', result)
else :
    print('Element does not exist.')
    
# $ python linear-search.py 
# Element found at index 4

# The time complexity of the above algorithm is O(n). 
# Linear search is rarely used practically because other search algorithms such as the 
# binary search algorithm and hash tables allow significantly faster-searching comparison to 
# Linear search.
# T.C = O(n)

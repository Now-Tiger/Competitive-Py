# Sort elements by frequency :
'''
1. Print the elements of an array in the decreasing frequency if 2 numbers have same frequency then print the one which came first. 
Examples:  
Input:  arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}

Input: arr[] = {2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999}

explanation :
  Input 5  2  2  8  5  6  8  8

  After sorting we get
  Element 2 2 5 5 6 8 8 8
  Index   1 2 0 4 5 3 6 7

  Now construct the 2D array as
  Index, Count
  1,      2
  0,      2
  5,      1
  3,      3

  Sort by count (consider indexes in case of tie)
  3, 3
  0, 2
  1, 2
  5, 1

  Print the elements using indexes in the above 2D array.
'''

from collections import Counter

initial_list = [2, 5, 2, 8, 5, 6, 8, 8]

print('Initial list :',str(initial_list))
result = [item for items, c in Counter(initial_list).most_common() for item in [items]*c]
print('Final result :', str(result))
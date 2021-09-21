__auther__ = 'Swapnil'
# --------------------------------------------- Reverse a string using Stack ---------------------------------------------

# You are given a string S, the task is to reverse the string using stack.

# Example 1:
# Input: S="GeeksforGeeks"
# Output: skeeGrofskeeG
 
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function reverse() which takes the 
# string S as an input parameter and returns the reversed string.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)

# ------------------------------------------------------------------------------------------------------------------------

from collections import deque
def reversestring(string) :
    stack = deque(string)
    return ''.join(stack.pop() for _ in range(len(stack)))

if __name__ == '__main__' :
    s = 'OneForAll'
    print(reversestring(s))


# Python program to reverse a string without stack

def reverse(string) :
    return string[::-1]

if __name__ == '__main__' :
    b = 'GeeksForGeeks'
    print(reverse(b))


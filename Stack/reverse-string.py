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

# Stack implementation using an empty list :

class Stack :
    def __init__(self) :
        self.stack = []
  
    def __bool__(self) :
        return not bool(self.stack)

    def __str__(self) :
        return str(self.stack)

    def size(self) :
        return len(self.stack)

    def isEmpty(self) :
        if len(self.stack) == 0 :
            return True

    def push(self, data) :
        self.stack.append(data) 

    def pop(self) :
        if self.stack :
            return self.stack.pop()
        else :
            raise IndentationError('pop empty stack!')
        
    def peek(self) :
        if self.stack :
            return self.stack[-1]

# Function to reverse the string :
def reverse(string) :
    n = len(string) 
    stack = Stack()
    for i in range(0, n, 1) :
        stack.push(string[i])
    string = ''
    for i in range(0, n, 1) :
        string += stack.pop()
    return string

# ---------------------------------------------- Using deque from collections --------------------------------------------

def reversestring(string) :
    stack = deque(string)
    return ''.join(stack.pop() for _ in range(len(stack)))

  
if __name__ == '__main__' :
    string = 'eciNtoNsiemanyM'
    string = reverse(string)
    print(f'Reversed string : {string}')
    print('-'*40)
    s = 'llAroFenO'
    print(f'Reversed string : {reversestring(s)}')

# $ python reverse-string.py 
# Reversed string : MynameisNotNice
# ----------------------------------------
# Reversed string : OneForAll

# T.C = O(N)            S.C = O(N)

# -------------------------------------------- Stack Implementation in Python -----------------------------------------------

# The stack can easily be implemented. Following is the custom stack implementation in Python.

# The stack supports the following standard operations:

# push: Pushes an item at the top of the stack.
# pop: Remove and return the item from the top of the stack.
# peek: Returns the item at the top of the stack without removing it.
# size: Returns the total number of items in the stack.
# isEmpty: Checks whether the stack is empty.
# isFull: Checks whether the stack is full.

# NOTE : stack implementation using dynamic array has many limitions. So the alernate approach is 'Repeated Doublig'.
#        Below code is representation of stack implementation using repeated doubling array apporach, 
#        which runs in O(n) complexity 

# ---------------------------------------------------------------------------------------------------------------------------

import random 

class Stack :
    def __init__(self, capacity = 1) :
        self.capacity = capacity
        self.top = - 1
        self.A = [None] * capacity
    
    def push(self, data) :
        if self.capacity == self.top + 1 :
            print('\nTrying to resize : Increasing')
            self.resize()
        if self.isFull() :
            print('Stack overflow')
            return
        self.top = self.top + 1
        self.A[self.top] = data
    
    def resize(self) :
        self.capacity  == self.capacity * 2
        newArray = [None] * self.capacity
        if newArray is None :
            print('Use big machine :( ')
            return
        for i in range(0, self.top + 1) :
            newArray[i] = self.A[i]
        self.A = newArray
    
    def isFull(self) :
        return self.capacity == self.top + 1

    def pop(self) :
        if self.top == - 1 :
            print('Stack uderflow')
            return
        temp = self.A[self.top]
        self.top = self.top - 1
        if self.top < self.capacity // 2 :
            print('\nTrying to resize : Decrese')
            self.capacity = self.capacity // 2 
            newArray = [None] * self.capacity
            for i in range(0, self.top + 1) :
                newArray[i] = self.A[i]
            self.A = newArray
        return temp

    def peek(self) :
        if self.top == -1 :
            print('Stack underflow')
            return
        return self.A[self.top]

    def isEmpty(self) :
        return self.top == -1

if __name__ == '__main__' :
    stack = Stack(capacity=10)
    ''' for _ in range(10) :
        stack.push(random.randint(1, 21))
    for _ in range(12) :
        temp = stack.pop()
        if temp is not None :
            print(temp)'''
    # comment out obove and erase capacity = 10, and put stack = Stack()
    # put comment on below code 
    stack.push(2)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())

# $ python stack.py
# 6

# Trying to resize : Decrese
# 6 
# 5

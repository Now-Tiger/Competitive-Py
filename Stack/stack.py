# -------------------------------------------- Stack Implementation in Python ---------------------------------------------

# The stack can easily be implemented. 

# Following is the custom stack implementation in Python using repeated doubling array implementation.

# The stack supports the following standard operations:

# push: Pushes an item at the top of the stack.
# pop: Remove and return the item from the top of the stack.
# peek: Returns the item at the top of the stack without removing it.
# size: Returns the total number of items in the stack.
# isEmpty: Checks whether the stack is empty.
# isFull: Checks whether the stack is full.

# -------------------------------------------------------------------------------------------------------------------------

import random 

class Stack :
    def __init__(self, capacity = 1) :
        self.capacity = capacity
        self.top = - 1
        self.A = [None] * capacity
    
    def push(self, data) :
        if self.capacity == self.top + 1 :
            print('Trying to resize : Increasing')
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
            print('Trying to resize : Decrese')
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
        return self.top == - 1
    
    def __repr__(self) :
        print( f'{self.A}')


def main() :
    stack = Stack(capacity=8)
    # for _ in range(10) :
    #     stack.push(random.randint(1, 21))
    # for _ in range(12) :
    #     temp = stack.pop()
    #     if temp is not None :
    #         print(temp)
    # comment out obove and erase capacity = 10, and put stack = Stack()
    # put comment on below code 
    
    stack.push(2)
    stack.push(4)
    stack.push(5)
    stack.__repr__()
    stack.push(6)
    stack.__repr__()
    stack.push(10)
    stack.__repr__()
    print(f'\nTop element : {stack.peek()}')
   
    print(f'\nStack empty ? : {stack.isEmpty()}')
    
    print('\nRemoving top element from stack : ')
    print(f'Removing element : {stack.pop()}')
    stack.__repr__()
    print(f'\nStack full ? : {stack.isFull()}')


if __name__ == '__main__' :
    main()


# $ python stack.py

# [2, 4, 5, None, None, None, None, None]
# [2, 4, 5, 6, None, None, None, None]
# [2, 4, 5, 6, 10, None, None, None]  

# Top element : 10

# Stack empty ? : False

# Removing top element from stack :   
# Trying to resize : Decrese
# Removing element : 10
# [2, 4, 5, 6]

# Stack full ? : True


# T.C = O(n) .

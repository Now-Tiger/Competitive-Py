# -------------------------------------------- Stack Implementation in Python ---------------------------------------------

# The stack can easily be implemented as a list. Following is the custom stack implementation in Python, which uses a list.

# The stack supports the following standard operations:

# push: Pushes an item at the top of the stack.
# pop: Remove and return the item from the top of the stack.
# peek: Returns the item at the top of the stack without removing it.
# size: Returns the total number of items in the stack.
# isEmpty: Checks whether the stack is empty.
# isFull: Checks whether the stack is full.

# -------------------------------------------------------------------------------------------------------------------------

class Stack :
    def __init__(self, limit = 10) :
        self.stack = []
        self.limit =  limit

    def __bool__(self) :
        return not bool(self.stack)

    def __str__(self) :
        return str(self.stack)

    def push(self, data) :
        if len(self.stack) >= self.limit :
            raise StackOverFlowError
        self.stack.append(data)
    
    def pop(self) :
        if self.stack :
            return self.stack.pop()
        else :
            raise IndexError('Pop from empty stack !!')

    def peek(self) :
        if self.stack :
            return self.stack[-1]

    def isEmpty(self) :
        return not bool(self.stack)

    def size(self) :
        return len(self.stack)


class StackOverFlowError(BaseException) :
    pass 


def main() :
    stack = Stack()
    for i in range(1, 11) :
        stack.push(i)

    print('\nStack demonstration :')
    print('-'*70)
    print('Initial stack: ' + str(stack))
    print('pop(): ' + str(stack.pop()))
    print('After pop(), the stack is now: ' + str(stack))
    print('peek(): ' + str(stack.peek()))
    stack.push(100)
    print('After push(100), the stack is now: ' + str(stack))
    print('isEmpty(): ' + str(stack.isEmpty()))
    print('size(): ' + str(stack.size()))

# -------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__' :
    main()

# -------------------------------------------------------------------------------------------------------------------------
# $ python stack.py 

# Stack demonstration :
# ----------------------------------------------------------------------
# Initial stack: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pop(): 10
# After pop(), the stack is now: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# peek(): 9
# After push(100), the stack is now: [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]   
# isEmpty(): False
# size(): 10



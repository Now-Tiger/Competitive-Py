### Problem : 

Show how you can efficiently implement one stack using two queues. Analyze the running time of the stack operations.

### Solution : 
- Yes it is possible to implement Stack ADT using two queues.  
- One of the queue will be used to store the elements and other one to hold them temporarily during pop and top methods.
- The pop method would enQueue the given element into the storage queue.
- Top method would transfer the all but last element from the storage queue onto temporary queue, save the front element of 
the storage queue to be returned, transfer the last element from the storage to the temporary queue, then transfer all the elements back
to the storage queue. 
- The __pop__ method would de do the same as top, except instead of the last element onto the temporary queue after saving it for return, that
last element would be discarded.
- Let __q1__ and __q2__ be the two queues to be used in the implementation of stack. 
- All we have to do is define push and pop operations on stack.

``` python

class Queue(object) :
    def __init__(self) :
        self.queue = []
    
    def isEmpty(self) :
        return (self.queue == [])

    def enQueue(self, item) :
        self.queue.append(item)

    def deQueue(self) :
        if self.queue :
            a = self.queue[0]
            self.queue.remove(a)
            return a
        else :
            raise IndentationError
    
    def size(self) :
        return len(self.queue)


class Stack(object) :
    def __init__(self) :
        self.q1 = Queue()
        self.q2 = Queue()
    
    def isEmpty(self) :
        return self.q1.isEmpty() and self.q2.isEmpty()
    
    def push(self, item) :
        if self.q2.isEmpty() :
            self.q1.enQueue(item)
        self.q2.enQueue(item)

    def pop(self) :
        if self.isEmpty() :
            raise IndentationError
        
        elif self.q2.isEmpty() :
            while not self.q1.isEmpty() :
                curr = self.q1.deQueue()
                if self.q1.isEmpty() :
                    return curr
                self.q2.enQueue(curr)
        else :
            while not self.q2.isEmpty() :
                curr = self.q2.deQueue()
                if self.q2.isEmpty() :
                    return curr
                self.q1.enQueue(curr)


if __name__ == '__main__' :
    stk = Stack()
    for i in range(5) :
        stk.push(i)
    for i in range(5) :
        print(stk.pop())


# $ python one-stack-using2-queues.py 
# 4
# 3
# 2
# 1
# 0

# Time Complexity : O(n)
```

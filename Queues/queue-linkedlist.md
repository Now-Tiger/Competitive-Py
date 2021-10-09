### Implementing queue using linked list.

- Another way of implementing queue is by using linked list.
- EnQueue operation is done by inserting an element at the end of list.
- DeQueue operation is done by deleting an element from the begining of the list.
``` python

class Node :
    def __init__(self, data = None, next = None) :
        self.data = data
        self.last = None
        self.next = next 

    def setData(self, data) :
        self.data = data
    
    def getData(self) :
        return self.data

    def setNext(self, next) :
        self.next = next

    def getNext(self) :
        return self.next

    def setLast(self, last) :
        self.last = last

    def getLast(self) :
        return self.last
    
    def hasNext(self) :
        return self.next != None

class Queue(object) :
    def __init__(self, data = None) :
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, data) :
        self.lastNode = self.front
        self.front = Node(data, self.front)
        if self.lastNode :
            self.lastNode.setLast(self.front)
        if self.rear is None :
            self.rear = self.front 
        self.size += 1

    def deQueue(self) :
        if self.rear is None :
            print('Sorry, the queue is empty')
            raise IndentationError
        result = self.rear.data
        self.rear = self.rear.last
        self.size -= 1
        return result

    def queueRear(self) :
        if self.rear is None :
            print('Sorry the queue is empty')
            raise IndentationError
        self.rear.data

    def queueFront(self) :
        if self.front is None :
            print('Sorry queue is empty')
            raise IndentationError
        self.front.data
    
    def size(self) :
        return self.size

if __name__ == '__main__' :
    q = Queue()
    q.enQueue('First')
    print(f'Front : {q.queueFront()}')
    print(f'Rear : {q.queueRear()}')

    q.enQueue('Second')
    print(f'Front : {q.queueFront()}')
    print(f'Rear : {q.queueRear()}')

    q.enQueue('Third')
    print(f'Front : {q.queueFront()}')
    print(f'Rear : {q.queueRear()}')

    print(f'Dequeue : {q.deQueue()}')

    print(f'Front : {q.queueFront()}')
    print(f'Rear : {q.queueRear()}')


```

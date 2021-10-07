
# ------------------------------------------------------ Queue using circular array implementation ------------------------------------------------------

class Queue(object) :
    def __init__(self, limit = 5) :
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self) :
        return self.size <= 0
    
    def enQueue(self, item) :
        if self.size >= self.limit :
            print('Queue Overflow')
            return
        else :
            self.que.append(item)
        if self.front is None :
            self.front = self.rear = 0
        else :
            self.rear = self.size
        self.size += 1

    def deQueue(self) :
        if self.size <= 0 :
            print('Queue underflow') 
            return 0
        else :
            self.que.pop(0)
            self.size -= 1
            if self.size == 0 : 
                self.front = self.rear = None
            else : 
                self.rear = self.size - 1
            print('\nQueue after deQueue', self.que)

    def queueRear(self) :
        if self.rear is None :
            print('Sorry the queue is empty ')
            raise IndexError
        return self.que[self.rear]

    def queueFront(self) :
        if self.front is None :
            print('Sorry the queue is empty')
            raise IndexError
        return self.que[self.front]

    def size(self) :
        return self.size


    def printqueue(self):
        return self.que


if __name__ == '__main__' :
    que = Queue()
    que.enQueue('fist')
    print(f'Front : {que.queueFront()}')
    print(f'Rear : {que.queueRear()}')
    print('\nAfter uploading second item : ')
    
    que.enQueue('second')
    print(f'Front : {que.queueFront()}')
    print(f'Rear : {que.queueRear()}')
    print('\nAfter uploading third item : ')
    
    que.enQueue('third')
    print(f'Front : {que.queueFront()}')
    print(f'Rear : {que.queueRear()}')
    
    print(f'\nOur queue : {que.printqueue()}')

    que.deQueue()
    print(f'Front : {que.queueFront()}')
    print(f'Rear : {que.queueRear()}')
    
    que.deQueue()
    print(f'Front : {que.queueFront()}')
    print(f'Rear : {que.queueRear()}')

    print(f'\nOur queue : {que.printqueue()}')

# $ python queue.py 
# Front : fist
# Rear : fist
# 
# After uploading second item : 
# Front : fist
# Rear : second
# 
# After uploading third item : 
# Front : fist
# Rear : third
#
# Our queue : ['fist', 'second', 'third']
#
# Queue after deQueue ['second', 'third']
# Front : second
# Rear : third
# 
# Queue after deQueue ['third']
# Front : third
# Rear : third
# 
# Our queue : ['third']
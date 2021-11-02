
# --------------------------- Dynamic circular array implementation of queue ---------------------------
# 

class Queue(object) :
    def __init__(self, limit = 5) :
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self) :
        return self.size <= 0

    def enQueue(self, data) :
        if self.size >= self.limit :
            self.resize()
        self.que.append(data)
        if self.front is None :
            self.front = self.rear = 0
        else :
            self.rear = self.size
        self.size += 1
        print(f'Queue after enQueue : {self.que}')

    def deQueue(self):
        if self.size <= 0 :
            print('Queue Underflow')
            return 0
        else :
            self.que.pop(0)
            self.size -= 1
            if self.size == 0 :
                self.front = self.rear = None
            else :
                self.rear = self.size - 1
            print(f'Queue after deQueue {self.que}')

    def queRear(self) :
        if self.rear is None :
            print('Sorr, the queue is empty!')
            raise IndexError
        return self.que[self.rear]

    def queFront(self) :
        if self.front is None :
            print('Sorry, the queue is empty!') 
            raise IndexError
        return self.que[self.front]
    
    def resize(self) :
        newQueue = list(self.que)
        self.limit = 2 * self.limit
        self.que = newQueue


if __name__ == '__main__' :
    q = Queue()
    q.enQueue('first')
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    q.enQueue('second')
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    q.enQueue('third')
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    q.enQueue('fourth')
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    q.enQueue('fifth')
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    q.enQueue('sixth')
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')


    
    q.deQueue()
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    q.deQueue()
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    q.deQueue()
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    q.deQueue()
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    q.deQueue()
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    q.deQueue()
    #print(f'Front : {q.queFront()}')  |\
    #print(f'Rear : {q.queRear()}')    | \ These two gives indexerrors as we mentioned
    
    q.enQueue(2)
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    q.enQueue(3)
    print(f'Front : {q.queFront()}')
    print(f'Rear : {q.queRear()}')
    
    print(q.isEmpty())


# $ python dynamic-circular-array.py 
# Queue after enQueue : ['first']
# Front : first
# Rear : first
# Queue after enQueue : ['first', 'second']
# Front : first
# Rear : second
# Queue after enQueue : ['first', 'second', 'third']
# Front : first
# Rear : third
# Queue after enQueue : ['first', 'second', 'third', 'fourth']
# Front : first
# Rear : fourth
# Queue after enQueue : ['first', 'second', 'third', 'fourth', 'fifth']
# Front : first
# Rear : fifth
# Queue after enQueue : ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
# Front : first
# Rear : sixth
# Queue after deQueue ['second', 'third', 'fourth', 'fifth', 'sixth']
# Front : second
# Rear : sixth
# Queue after deQueue ['third', 'fourth', 'fifth', 'sixth']
# Front : third
# Rear : sixth
# Queue after deQueue ['fourth', 'fifth', 'sixth']
# Front : fourth
# Rear : sixth
# Queue after deQueue ['fifth', 'sixth']
# Front : fifth
# Rear : sixth
# Queue after deQueue ['sixth']
# Front : sixth
# Rear : sixth
# Queue after deQueue []
# Queue after enQueue : [2]
# Front : 2
# Rear : 2
# Queue after enQueue : [2, 3]
# Front : 2
# Rear : 3
# False
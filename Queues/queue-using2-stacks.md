### Problem : 
How can you implement queue using two stacks ?

``` python
class Queue(object) :
    def __init__(self) :
        self.S1 = []
        self.S2 = []
    
    def enQueue(self, item) :
        self.S1.append(item)
    
    def deQueue(self) :
        if not self.S2 :
            while self.S1 :
                self.S2.append(self.S1.pop())
        return self.S2.pop()
    
if __name__ == '__main__' :
    queue = Queue()
    for i in range(5) :
        queue.enQueue(i)
    for i in range(5) :
        print(queue.deQueue(), end = ' ') 

# $ python queue-using2-stacks.py 
# 0 1 2 3 4 
```

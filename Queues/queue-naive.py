#!/yar/bin/ pypy3
# -*- coding: utf-8 -*-
# ----------------------------- Queue implementation using array -----------------------------

class Queue :
    def __init__(self) :
        self.items = []

    def is_empty(self) :
        return self.items == []
    
    # Add elemets into queue
    def enqueue(self, data) :
        self.items.append(data)

    # Pop/remove elements from queue
    def dequeue(self) :
        return self.items.pop(0)

    # Display queue 
    def display(self) :
        return self.queue

def main() :
    queue = Queue()
    queue.enqueue('google')
    queue.enqueue('youtube')
    queue.enqueue('udemy')
    queue.enqueue('udacity')
    print(queue.display())
    queue.dequeue()
    queue.dequeue()
    print(queue.display())


# Driver code
if __name__ == '__main__' :
    main()

# $ pypy3 queue.py 
# ['google', 'youtube', 'udemy', 'udacity']
# ['udemy', 'udacity']




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
        arr = []
        for i in self.items :
            arr.append(i)
        return arr

def main() :
    queue = Queue()
    queue.enqueue('google')
    queue.enqueue('youtube')
    queue.enqueue('udemy')
    queue.enqueue('udacity')
    queue.dequeue()
    queue.dequeue()
    print(queue.display())


# Driver code
if __name__ == '__main__' :
    main()

# $ python queue.py 
# ['udemy', 'udacity']



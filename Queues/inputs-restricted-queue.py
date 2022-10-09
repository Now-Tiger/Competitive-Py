#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

# --------------------- Implementation of Input Restricted Queue ------------------------

# Input restricted Queue: In this type of Queue, the input can be taken from one side
# only(rear) and deletion of elements can be done from both sides(front and rear).
# This kind of Queue does not follow FIFO(first in first out).

class Deque(object):
    """ Input restricted queue naming it as Deque. """

    def __init__(self, limit: int) -> None:
        self.queue = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data: int) -> None:
        if self.size >= self.limit:
            print("Queue overflow ...")
            return
        else:
            self.queue.append(data)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1

    def dequeue_front(self) -> None:
        """ Method to delete element from front of the queue """
        if self.size <= 0:
            print("Queue underflow")
            return
        else:
            self.queue.pop()
            self.size -= 1
        if self.size == 0:
            self.front = self.rear = None
        else:
            self.rear = self.size - 1
        print(f"queue after deletion from front: {self.queue}")

    def dequeue_rear(self) -> None:
        """ Method to delete element from rear of the queue """
        if self.size <= 0:
            print("Queue underflow")
            return
        else:
            self.queue.pop(0)
            self.size -= 1
        if self.size == 0:
            self.front = self.rear = None
        else:
            self.rear = self.size - 1
        print(f"queue after deletion from rear: {self.queue}")

    def queue_front(self) -> int:
        if self.front is None:
            print(f"sorry queue is empty")
        return self.queue[self.front]

    def queue_rear(self) -> int:
        if self.rear is None:
            print(f"sorry queue is empty")
        return self.queue[self.rear]

    def is_empty(self) -> bool:
        return self.size <= 0

    def size(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str(self.queue)


if __name__ == "__main__":
    q = Deque(5)

    lis = [1, 2, 3, 4, 5, 6, 7]

    for i in lis:
        q.enqueue(i)
    print(q)

    print(f"is queue empty ?\n- {q.is_empty()}")
    q.dequeue_rear()
    q.dequeue_front()

    print(q.queue_front())
    print(q.queue_rear())


# $ pypy3 inputs-restricted-queue.py
# Queue overflow ...
# Queue overflow ...
# [1, 2, 3, 4, 5]
# is queue empty ?
# - False
# queue after deletion from rear: [2, 3, 4, 5]
# queue after deletion from front: [2, 3, 4]
# 2
# 4

#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-

# --------------------- Output restricted Queue ---------------------
# In this type of Queue, the input can be taken from both sides(rear and front)
# and the deletion of the element can be done from only one side(front).


class Deque(object):
    """ Output restricted queue naming it as Deque. """

    def __init__(self, limit: int) -> None:
        self.queue = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue_front(self, data: int) -> None:
        """ Add element from front of the queue. """
        if self.size >= self.limit:
            print("Queue overflow")
            return
        else:
            self.queue.append(data)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1

    def enqueue_rear(self, data: int) -> None:
        """ Add element from the rear of the queue. """
        if self.size >= self.limit:
            print("Queue overflow")
            return
        else:
            self.queue.insert(0, data)
        if self.rear is None:
            self.rear = self.front = 0
        else:
            self.rear = self.size
        self.size += 1

    def dequeue_front(self) -> None:
        """ Remove element from front of the queue. """
        if self.size <= 0:
            print("Queue is empty")
            return
        else:
            self.queue.pop()
            self.size -= 1
        if self.size == 0:
            self.front = self.rear = None
        else:
            self.rear = self.size - 1
        print(f"Queue after deletion from front: {self.queue}")

    def print_queue(self) -> None:
        print(f"{self.queue}")

    def size(self) -> int:
        return self.size

    def empty(self) -> bool:
        return self.size <= 0


if __name__ == "__main__":
    q = Deque(5)
    q.enqueue_front(1)
    q.enqueue_front(2)
    q.enqueue_front(3)
    q.enqueue_front(4)
    q.enqueue_rear(5)
    q.enqueue_rear(6)
    q.enqueue_rear(7)

    q.print_queue()

    print(f"is queue empty ?\n- {q.empty()}")
    q.dequeue_front()


# $ pypy3 output-restricted-queue.py
# Queue overflow
# Queue overflow
# [5, 1, 2, 3, 4]
# is queue empty ?
# - False
# Queue after deletion from front: [5, 1, 2, 3]

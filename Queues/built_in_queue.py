#!/usr/bin/ pypy3
# -*- coding: utf-8 -*- 

from __future__ import annotations
from queue import Queue

# -- Playing arround built-in queue module. 
# ** Note: Please do not follow this code since it is a very messy code. 

class Queue_ops(object):
    def __init__(self, que: Queue) -> None:
        self.que = que

    def add_elements(self, elements: list) -> Queue:
        """ 
            Here adding elements from an array to
            the queue.
        """
        if  len(elements) == 0:
            print(f'empty list of elements: {elements}')
            return
        for element in elements:
            self.que.put(element)
        return self.que

    def print_elements(self) -> str:
        """ Queue is not an iterable object """
        if self.que.empty():
            print('First insert elements in the queue...')
            
        while not self.que.empty():
            item = self.que.get()
            print(item, end = ", ")
        return
    

def main() -> None:
    q = Queue()
    que = Queue_ops(q)
    que.print_elements()
    elements = [11, 22, 54, 88, .65]
    que.add_elements(elements)
    que.print_elements()
    return


if __name__ == "__main__":
    main()
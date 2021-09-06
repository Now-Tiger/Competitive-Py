# [Queues](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
In computer science, __a queue is a collection of entities that are maintained in a sequence and can be modified by the addition of entities at one end of the sequence and the removal of entities from the other end of the sequence.__ 

By convention, the end of the sequence at which elements are __added__ is called the __back, tail, or rear of the queue__, and the end at which elements are __removed__ is called the __head or front__ of the queue, analogously to the words used when people line up to wait for goods or services.

The operations of a queue make it a __first-in-first-out (FIFO)__ data structure. In a FIFO data structure, the first element added to the queue will be the first one to be removed. This is equivalent to the requirement that once a new element is added, all elements that were added before have to be removed before the new element can be removed. A queue is an example of a linear data structure, or more abstractly a sequential collection. Queues are common in computer programs, where they are implemented as data structures coupled with access routines, as an abstract data structure or in object-oriented languages as classes. Common implementations are circular buffers and linked lists.

Queues provide services in computer science, transport, and operations research where various entities such as data, objects, persons, or events are stored and held to be processed later. In these contexts, the queue performs the function of a buffer. Another usage of queues is in the implementation of breadth-first search.

![image](https://miro.medium.com/max/1400/0*TRbfsq86lqDoqW6b.png)

# Queue ADT

The following operations make a queue an ADT. Insertions and deletions in a queue must follow the FIFO scheme. For simplicity, we assume the elements are integers.

Main Queue Operations:

- enQueue(int data): Inserts an element at the end of the queue

- int deQueue(): Removes and returns the element at the front of the queue.

 

# Applications:

- Operating systems schedule jobs (with equal priority) in the order of arrival (e.e a print queue).

- Simulation of real-world queues such as lines at a ticket counter, or any other first-come first-served scenario requires a queue.

- Multiprogramming.

- Asynchronous data transfer (file IO, pipes, sockets).

- Waiting times for a customer at a call center.

- Determining the number of cashiers to have at a supermarket.

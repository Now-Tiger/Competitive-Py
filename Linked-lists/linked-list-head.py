
# A Linked List node consists of a data field and a reference to the next node in the list. 
# We can use a constructor to initialize the data and the next field for a node allocated in the memory during runtime.

class Node(object):
    def __init__(self, value) :
        # set data
        self.value = value 
        # set the next field to point to a given node of the list
        self.next = None 




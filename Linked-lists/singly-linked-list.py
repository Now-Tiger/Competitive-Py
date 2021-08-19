
# create singly linked list :

class Node(object) :
    def __init__(self, value) :
        self.value = value 
        self.next_val = None

class SLinkedList(object) :
    def __init__(self) :
        self.head_val = None

    def printlist(self) :
        printval = self.head_val
        while printval is not None :
            print(printval.value, end = ' -> ')
            printval = printval.next_val
        print('None')

list = SLinkedList()
list.head_val = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')
e4 = Node('Thurs')

list.head_val.next_val = e2
e2.next_val = e3
e3.next_val = e4
list.printlist()

# output :
# Mon
# Tue
# Wed
# Thurs

# Mone -> Tue -> Wed -> Thurs
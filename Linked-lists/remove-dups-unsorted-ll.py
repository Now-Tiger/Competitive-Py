
class Node(object):
    def __init__(self, value):
        self.value = value 
        self.next = None

class Linkedlist(object) :
    def __init__(self) :
        self.head = None

    def printlist(self) :
        printval = self.head
        while printval is not None :
            print(printval.value, end = ' -> ')
            printval = printval.next
        print('None')
    
    def remove_dups(self) :
        current = self.head
        prev = None
        duplicate_dict = dict()
        while current :
            if current.value not in duplicate_dict :
                duplicate_dict[current.value] = None
                prev = current
            else :
                prev.next = current.next
            
            current = current.next  

l = Linkedlist()
l.head = Node(25)
e2, e3, e4, e5, e6, e7 = Node(35), Node(15), Node(32), Node(25), Node(80), Node(15)
l.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
l.printlist()

l.remove_dups()
print('\nAfter removal of duplicates\n----------------------------------------\n')
l.printlist()
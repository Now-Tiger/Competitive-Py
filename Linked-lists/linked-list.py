# ---------------------------------------------------- Implement singly linked list ----------------------------------------------------
#
# operations on linked list :
# Insertion of an element
# Deletion of an element
# traversing the list
# Search an element
#
# --------------------------------------------------------------------------------------------------------------------------------------

class Node :
    def __init__(self, data ) :
        self.data = data
        self.next = None

class Linkedlist :
    def __init__(self, head = None) :
        self.head = head 

    # Search an element in the list :
    def search(self, list, key) :
        if not list : 
            return False 
        if list.data == key : 
            return True
        return self.search(list.next, key)
    
    def delete(self, value) :
        """
            1. If the head itself holds the value to be deletd.
            2. else search for the value in the linked list,
               also keep track of previous node as we need to change 
               'prev.next'
            ------------------------
            function returns nothing
            ------------------------
            to check use printlist() function.
        """
        temp = self.head
        if (temp is not None):
            if temp.data == value:
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None
    
    # print the linked list : elements :
    def printlist(self) :
        if self.head == None :
            raise ValueError('Empty list !')
        current = self.head
        while current :
            print(current.data, end = '->')
            current = current.next
        print('null')

    # Find length of the linked list :
    def size(self) :
        if self.head == None :
            return 0
        size = 0
        current = self.head
        while current :
            size += 1
            current = current.next
        print(size) 
    
    # Insert node in the begining :
    def insertAtBegining(self, data) :
        newnode = Node(data)
        if self.size == 0 :
            self.head = newnode
        else :
            newnode.next = self.head
            self.head = newnode
        
    # Insert node at ending :
    def insertAtEnding(self, data) :
        newnode = Node(data)
        current = self.head
        while current.next != None :
            current = current.next
        current.next = newnode


if __name__ == "__main__":
    list = Linkedlist()
    list.head = Node(1)
    second = Node(2)
    third = Node(3)
    list.head.next = second
    second.next = third

    print('\nInitial linked list :')
    list.printlist()

    print('\nInserting 0 at begining : ')
    list.insertAtBegining(0)

    list.printlist()
    print('\nInserting 5 at ending :')

    list.insertAtEnding(5)
    list.printlist()

    print('\nSize of linked-list :')
    list.size()

    print('\nSearch element 6 in the list :')
    key = 6
    if list.search(list.head, key):
        print(f'{key} is present')
    else:
        print(f'{key} is not present')

    print("\ndeleting node 5")
    list.delete(5)
    list.printlist()


# $ python linked-list.py

# Initial linked list :
# 1->2->3->null

# Inserting 0 at begining :
# 0->1->2->3->null

# Inserting 5 at ending :
# 0->1->2->3->5->null

# Size of linked-list :
# 5

# Search element 6 in the list :
# 6 is not present

# deleting node 5
# 0->1->2->3->null

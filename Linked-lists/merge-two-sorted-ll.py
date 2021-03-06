# 21
# ------------------------------------------------ Merge Two Sorted Lists ------------------------------------------------

# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of
# the first two lists.

# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# ------------------------------------------------------------------------------------------------------------------------

class ListNode:
    def __init__(self, value=0):
        self.value = value
        self.next = None

    def printlist(self):
        printval = self
        while True:
            print(printval.value, end=' ')
            printval = printval.next
            if not printval:
                break
            else:
                print('->', end=' ')
        print()

class Solution:
    def mergetwolists(self, l1, l2):
        dummy = ListNode(0) 
        temp = dummy
        while l1 and l2:
            if l1.value <= l2.value:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2  # if any l1 or l2 = None temp point to the remaning list
        return dummy.next     # as dummy point to 0 define initially

# ------------------------------------------------------ Tests ----------------------------------------------------------

def main():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(4)
    a.next = b
    b.next = c
    print('List 1 : ')
    a.printlist()

    aa = ListNode(1)
    bb = ListNode(3)
    a1 = ListNode(4)
    aa.next = bb
    bb.next = a1
    print('List 2 : ')
    aa.printlist()

    class_instance = Solution()
    res = Solution.mergetwolists(class_instance, a, aa)
    print('Merged list')
    if res:
        res.printlist()

# ------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

# ------------------------------------------------------------------------------------------------------------------------

# $ python merge-two-sorted-ll.py
# List 1 :
# 1 -> 2 -> 4
# List 2 :
# 1 -> 3 -> 4
# Merged list
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 

# T.C = O(M + N)


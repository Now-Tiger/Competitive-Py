
# ---------------------------------------------------- Min Heap Implementation ----------------------------------------------------

class heap(object) :
    def __init__(self) :
        self.heapList = [0]
        self.size = 0

    def parent(self, index) :
        return index // 2 

    def leftchild(self, index) :
        return 2 * index

    def rightchild(self, index) :
        return 2 * index + 1

    def getminimum(self) :
        if self.size == 0 :
            return -1
        return self.heapList[1]

    def percolateDown(self, i) :
        while (i * 2) <= self.size :
            minimumChild = self.minChild(i)
            if self.heapList[i] > self.heapList[minimumChild] :
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[minimumChild]
                self.heapList[minimumChild] = temp
            i = minimumChild
    
    def minChild(self, i) :
        if (i * 2 + 1) > self.size :
            return i * 2
        else :
            if self.heapList[i * 2] < self.heapList[i * 2 + 1] :
                return i * 2
            else :
                return i * 2 + 1
    
    def percolateUp(self, i) :
        while (i//2) > 0 :
            if self.heapList[i] < self.heapList[i//2] :
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def insert(self, k) :
        self.heapList.append(k)
        self.size += 1
        self.percolateUp(self.size)

    # heapify the array :
    def buildHeap(self, A) :
        i = len(A) // 2 
        self.size = len(A)
        self.heapList = [0] + A[:]
        while (i > 0) :
            self.percolateDown(i)
            i -= 1

    def printHeap(self) :
        if self.heapList is None :
            return 0
        return self.heapList

if __name__ == '__main__' :
    Heap = heap()
    A = [1, 20, 5, 100, 12, 18, 16]
    Heap.buildHeap(A)
    print(f'Original heap : {Heap.printHeap()}')

    print(f'Minimum element : {Heap.getminimum()}')
    print(f'Parent index is element 100 : {Heap.parent(4)}')
    print('Adding element 88 into the heap.')
    Heap.insert(88)
    print(f'New heap : {Heap.printHeap()}')
    print(f'Parent index of element 100 : {Heap.parent(8)}')


# $ python minheap.py
# Original heap : [0, 1, 12, 5, 100, 20, 18, 16]
# Minimum element : 1
# Parent index is element 100 : 2
# Adding element 88 into the heap.
# New heap : [0, 1, 12, 5, 88, 20, 18, 16, 100]
# Parent index of element 100 : 4


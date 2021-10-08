### Problem : 
  _Given an array A, the span S[i] of A[i] is the maximum number of consecutive elements A[j] immediately._

  __Another way of asking__ : _Given an array A of integers, find the maximum of j - i sujected to the constraints of A[i] < A[j]_

 -------------------------------------------------------------------------------------------------------------------------------------------------
``` python

# The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to 
# calculate span of stock’s price for all n days. 
# The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the 
# given day, for which the price of the stock on the current day is less than or equal to its price on the given day. 
# For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for 
# corresponding 7 days are {1, 1, 1, 2, 1, 4, 6} 
--------------------------------------------------------------------------------------------------------------------------

class Stack :
    def __init__(self) :
        self.items = []

    def push(self, item) :
        self.items.append(item)
    
    def pop(self) :
        return self.items.pop()

    def isEmpty(self) :
        return (self.items == [])

    def peek(self) :
        return self.items[-1]

    def __str__(self) :
        return str(self.items)

def findspan(A) :
    D = Stack()
    S = [None] * len(A)
    for i in range(0, len(A)) :
        while not D.isEmpty() and A[i] > A[D.peek()] :
            D.pop()
        if D.isEmpty() :
            P = -1
        else : 
            P = D.peek()
        S[i] = i - P
        D.push(i)
    print(S)

if __name__ == '__main__' :
    A = [6, 3, 4, 5, 2]
    findspan(A)


# $ python span-of-stock.py 
# [1, 1, 2, 3, 1]

```
Time Complexity : O(n)

Space Complexity : O(n) [for stack]

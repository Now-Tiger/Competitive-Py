
``` python
# ---------------------- The Stock Span Problem : Naive Approach ----------------------


def findspan(A) :
    Span = [None] * len(A)
    Span[0] = 1
    for i in range(0, len(A)) :
        Span[i] = 1
        j = i - 1
        while j >= 0 and A[i] >= A[j] :
            Span[i] += 1
            j -= 1
    for i in range(len(Span)) :
        print(Span[i], end = ' ')


if __name__ == '__main__' :
    A = [6, 3, 4, 5, 2]
    S = [None] * len(A)
    findspan(A)
   

# $ python span-of-stock-naive.py 
# 1 1 2 3 1 

# Time Complexity : O(n^2)
``` 

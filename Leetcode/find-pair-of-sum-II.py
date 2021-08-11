
# Problem statement : Find a pair with the given sum in an unsorted array. t(c) = o(n.logn)

def findpair(A, sum) :
    A.sort()
    (left, right) = (0, len(A)-1)
    
    while left <= right :
        if A[left] + A[right] == sum :
            print('Pair found:',(A[left], A[right]))
            return
        elif sum > A[left] + A[right] :
            left = left + 1
        else :
            right = right - 1
    
    print('Pair not found.')

if __name__ == '__main__':
 
    A = [8, 7, 2, 5, 3, 1]
    sum = 10
 
    findpair(A, sum)
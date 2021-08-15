

def isSubset(A1, A2, m, n) :
    hashset = set(A1)

    # loop to store all the values of A1
    #for i in range(0, m) :
    #    hashset.add(A1[i]) 

    # loop to check all the elements of A2
    # lies in A2 or not :
    for i in range(0, n) :
        if A2[i] in hashset :
            continue
        else :
            return False

    return True

if __name__ == "__main__":
    
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 1, 7]

    m = len(arr1)
    n = len(arr2)

    if(isSubset(arr1, arr2, m, n)):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[]")

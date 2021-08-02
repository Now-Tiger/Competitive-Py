# Q. 1 - 
#  A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .
#  Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product 
#  and False otherwise. (If m is not positive, your function should return False.)

def primeproduct(m) :
    x = [] 
    for i in range(2, m+1) :
        for j in range(2, i) :
            if (i % j == 0) :
                break
        else :
            x.append(i)
    for i in range(0, len(x)) :
        for j in range(0, len(x)) :
            if (x[i] * x[j] == m) :
                return True
    return False

print(primeproduct(188))



# Q. 2 - Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 (i.e., a single character), 
# and returns the string obtained by deleting all occurrences of c in s. If c has length other than 1, the function should return s

def delchar(s, c) :
    if len(c) == 1 :
        s = s.replace(c, '')
        return s
    else :
        return s;

print(delchar("banana","n"))



# Q.3 - Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting of the first elment in l1, 
# then the first element in l2, then the second element in l2, then the second element in l2, and so on. If the two lists are not of equal length, 
# the remaining elements of the longer list are appended at the end of the shuffled output.

def shuffle(l1,l2):
    c=[]
    if len(l1)!=0 and len(l2)!=0:
      for i in range(min(len(l1), len(l2))):
        c.extend([l1[i],l2[i]])      
      c.extend(l1[i+1:] or l2[i+1:])
    else:
      c.extend(l1[0:] or l2[0:])      
    return (c)

